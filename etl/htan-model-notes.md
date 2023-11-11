# HTAN data model

HTAN keeps its model here: https://github.com/ncihtan/data-models.git
in two formats: a CSV and a JSON-LD.

HTAN conversion of its CSV to JSON-LD creates a number of nodes with illegal chars in their IRIs (parens, greater than, less than, equals signs, carets)


CSV file - describes ~700 'Attributes'

Parent: Each Attribute has a 'Parent' assigned (Parents themselves come from the Attributes list)
- a handful of Attributes are not assigned a parent - 
- a tag that groups attributes
DependsOn Component: 
- another tag that groups attributes

Source: URL if available of the semantic source of the Attribute - not necessarily an "IRI", can be just a link


NOTE: Python module rdflib can parse jsonld - however, to be able to see the entities in the result object, must remove the top-level "@id" dict entry.

use virtualenv .../htan-venv

The entire graph contains a large number of triples:

    >>> g = rdflib.Graph().parse("HTAN.model.jsonld")
    >>> len(g)
    60020

There are however a limited number of unique predicates:

    >>> for x in {y for y in g.predicates()}:
    ...   print(x)
    ... 
    http://www.w3.org/2000/01/rdf-schema#subClassOf
    http://schema.org/isPartOf
    http://www.w3.org/1999/02/22-rdf-syntax-ns#type
    sms:requiresDependency
    http://schema.org/domainIncludes
    sms:required
    sms:displayName
    http://www.w3.org/2000/01/rdf-schema#label
    sms:validationRules
    http://www.w3.org/2000/01/rdf-schema#comment
    http://schema.org/rangeIncludes
    sms:requiresComponent
    >>>

RDF types represented (objects of http://www.w3.org/1999/02/22-rdf-syntax-ns#type) are 3:

DataType: rdflib.term.URIRef('http://schema.org/DataType')
Class: rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#Class')
Property: rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#Property')


In rdflib:

Representing a node like "http://www.w3.org/2000/01/rdf-schema#subClassOf" in rdflib:

- `rdflib.term.URIRef("http://www.w3.org/2000/01/rdf-schema#subClassOf")`

Representing a term with a prefix that isn't mapped to a URI (like "sms:requiresComponent"):

- `rdflib.term.Literal("sms:requiresComponent")`

You can import the namespaces of schema.org (SDO), rdf, rdfs, others

    >>> from rdflib.namespace import SDO
    >>> SDO.isPartOf
    rdflib.term.URIRef('https://schema.org/isPartOf')

Unfortunately, the HTAN predicates use the "http://" scheme for schema.org rather than 
the "https://" scheme, so the search `g.subject_objects(SDO.domainIncludes)` returns no
matches, while `g.subject_objects(rdflib.term.URIRef('http://schema.org/domainIncludes'))]`
does match. Tweak HTAN.model.jsonld to set

        "schema": "https://schema.org/"

(This is probably correct usage (http) - it appears that ontology
names are http in Protege, even if the resolving URI is https)

There are 12 unique objects of SDO.domainIncludes, out of 75 triples.
There are 450 unique subjects of SDO.rangeIncludes, out of 9121 triples.

Fundamental question: which entities are nodes, which are properties, which are terms?
There are 19208 unique entities:

    >>> obj = {x for x in g.objects(unique=True)}
    >>> len(obj)
    19073
    >>> sbj = {x for x in g.subjects(unique=True)}
    >>> len(sbj)
    7140
    >>> len(obj.union(sbj))
    19208

203 entities are required:

    >>> req = {x for x in g.subjects(uriref('sms:required'),literal('sms:true'))}
    >>> len(req)
    203

what types are these? All Classes except 2 (Property): fileFormat, filename

    >>> { y for y in req if g.value(y, RDF.type) == RDF.Property }
    {rdflib.term.URIRef('http://schema.biothings.io/fileFormat'), rdflib.term.URIRef('http://schema.biothings.io/filename')}

examine one entity: rdflib.term.URIRef('http://schema.biothings.io/Diagnosis'):

    >>> dx = rdflib.term.URIRef('http://schema.biothings.io/Diagnosis')
    >>> {x for x in g.predicates(dx,None) }
    {rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label'), rdflib.term.URIRef('sms:displayName'), rdflib.term.URIRef('https://schema.org/isPartOf'), rdflib.term.URIRef('sms:requiresDependency'), rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type'), rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#comment'), rdflib.term.URIRef('sms:required'), rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#subClassOf')}

dx has (is subject of) label, displayName, isPartOf, requiresDependency, type(Class), comment, required(no), subClassOf (is a subclass)
- is a subclass of Patient

dx is (is object of) requiresComponent (is a required component of), subClassOf (has subclasses)
- is a required component of rdflib.term.URIRef('http://schema.biothings.io/Patient')
- is a subclass of 97 enities, with examples:

        AdditionalTopography
        PrimaryDiagnosis
        YearofDiagnosis
        ExtentofTumorResection
        Laterality
        MarginsInvolvedSite
        GleasonGradeTertiary
        PrecancerousConditionType

So the relationship/predicate "subClassOf" is being interpreted as
"comes under the heading of" or "is part of group". It doesn't have
the semantic meaning of class inheritance. They could more effectively
use SKOS predicates. The use here is associative, no hierarchical
(broader/narrower) in SKOS parlance. But the semantics here is not
SKOS:related, because the relationship is not symmetric - it is a
"contained by" meaning.

The SKOS idea of a Collection might be applied, with each of the
target entities being asserted as a SKOS:Concept or a
SKOS:Collection. Then Concepts could be SKOS:members of the
aggregative entities. Now we're seeing a more meaningful
interpretation: that an mdf:Node is like a collection, and a
mdf:Property is like a concept. This isn't perfect though, because in
mdf, Nodes (and Relationships) can also "be" concepts. No that isn't
true, they can _have_ mdf:Concepts.

- So maybe mdf:Node and mdf:Relationship should be subclasses of SKOS:Collection
- and mdf:Property should be a subclass of SKOS:Concept? No that's too confusing. 
- mdf:Concept should be a subclass of SKOS:Concept.
- however, SKOS:member can apply to both Concepts and Collections *
- hmmm.

- But the idea is, can the mdf Model be embedded in SKOS, such that
  any mdf instance is consistent with SKOS? - might be cool.

so there are these made-up predicates:
- sms:displayName <- just a property
- sms:required <- just a property
- sms:validationRules 
- sms:requiresComponent
- sms:requiresDependency

What are the "required components" of Patient?

    >>> rqc_p = rdflib.term.URIRef('sms:requiresComponent')
    >>> for y in {x for x in g.objects(pt,rqc_p)}:
    ...   print(y.split('/')[-1])
    ... 
    FollowUp
    Exposure
    Therapy
    FamilyHistory
    Demographics
    MolecularTest
    Diagnosis


so we have a Patient Node with some subordinate Nodes. How are Properties indicated?
What are the "required dependencies" of Followup?

    >>> fu = rdflib.term.URIRef('http://schema.biothings.io/FollowUp')
    >>> rqd_p = rdflib.term.URIRef('sms:requiresDependency')
    >>> len({x for x in g.objects(fu,rqd_p)})
    51
    >>> for y in {x for x in g.objects(fu,rqd_p)}:
    ...   print(y.split('/')[-1])
    ... 
    BMI
    BarrettsEsophagusGobletCellsPresent
    MenopauseStatus
    AdverseEventGrade
    RecistTargetedRegionsSum
    RiskFactorTreatment
    Component
    KarnofskyPerformanceStatus
    ViralHepatitisSerologies
    PregnancyOutcome
    DaystoComorbidity
    ComorbidityMethodofDiagnosis
    DaystoAdverseEvent
    Height
    ImagingResult
    Weight
    ImagingType
    ScanTracerUsed
    FEV1RefPostBronchPercent
    DaystoImaging
    HAARTTreatmentIndicator
    HTANParticipantID
    EvidenceofRecurrenceType
    PancreatitisOnsetYear
    HysterectomyMarginsInvolved
    RiskFactor
    HPVPositiveType
    NadirCD4Count
    HysterectomyType
    HormonalContraceptiveUse
    HIVViralLoad
    CDCHIVRiskFactors
    AdverseEvent
    BodySurfaceArea
    CauseofResponse
    Comorbidity
    DaystoFollowUp
    ProgressionorRecurrence
    AIDSRiskFactors
    DiabetesTreatmentType
    CD4Count
    ImmunosuppressiveTreatmentType
    RecistTargetedRegionsNumber
    FEV1FVCPreBronchPercent
    DiseaseResponse
    DLCORefPredictivePercent
    ECOGPerformanceStatus
    FEV1RefPreBronchPercent
    FEV1FVCPostBronchPercent
    HepatitisSustainedVirologicalResponse
    RefluxTreatmentType

So it looks like all of these 'dependencies' are variables that can
contain data. Are these entities annotated in a way that indicates
they are variables/properties (besides being the object of the requiresDependency
predicate)

CD4Count - should be a simple type

    >>> cd4
    rdflib.term.URIRef('http://schema.biothings.io/CD4Count')

CD4Count only has a comment attached.

    >>> for y in {x for x in g.triples((cd4,None,None))}:
    ...   print("{}\t{}".format(y[1].split('/')[-1],y[2]))
    ... 
    sms:displayName	CD4 Count
    rdf-schema#subClassOf	http://schema.biothings.io/FollowUp
    isPartOf	http://schema.biothings.io
    rdf-schema#comment	The text term used to describe the outcome of the procedure to 
                        determine the amount of the CD4 expressing cells in a sample.
    22-rdf-syntax-ns#type	http://www.w3.org/2000/01/rdf-schema#Class
    sms:required	sms:false
    rdf-schema#label	CD4Count

AdverseEventGrade - should have acceptable values
Now we're getting somewhere: SDO.rangeIncludes evidently points to acceptable values

    >>> aeg
    rdflib.term.URIRef('http://schema.biothings.io/AdverseEventGrade')
    >>> for y in {x for x in g.triples((aeg,None,None))}:
    ...   print("{}\t{}".format(y[1].split('/')[-1],y[2]))
    ... 
    rdf-schema#comment	The text term used to describe a specific histone variants, which are proteins that substitute for the core canonical histones.
    rangeIncludes	http://schema.biothings.io/Grade4
    rangeIncludes	http://schema.biothings.io/Grade2
    sms:displayName	Adverse Event Grade
    rdf-schema#subClassOf	http://schema.biothings.io/FollowUp
    rdf-schema#label	AdverseEventGrade
    isPartOf	http://schema.biothings.io
    rangeIncludes	http://schema.biothings.io/Grade5
    22-rdf-syntax-ns#type	http://www.w3.org/2000/01/rdf-schema#Class
    rangeIncludes	http://schema.biothings.io/Grade3
    sms:required	sms:false
    rangeIncludes	http://schema.biothings.io/Grade1
    >>>

Acceptable value list (of Terms; possibly not Term values) for AdverseEventGrade:

    >>> for y in {x for x in g.objects(aeg,SDO.rangeIncludes)}:
    ...   print(y.split('/')[-1])
    ... 
    Grade3
    Grade5
    Grade1
    Grade4
    Grade2

Grade1 as a Term (i.e., rdflib.term.URIRef('http://schema.biothings.io/Grade1')) has
label, displayName, no explicitly specified value in mdf parlance:

    >>> grd1_t
    rdflib.term.URIRef('http://schema.biothings.io/Grade1')
    >>> for y in {x for x in g.triples((grd1_t,None,None))}:
    ...   print("{}\t{}".format(y[1].split('/')[-1],y[2]))
    ... 
    22-rdf-syntax-ns#type	http://www.w3.org/2000/01/rdf-schema#Class
    rdf-schema#subClassOf	http://schema.biothings.io/AdverseEventGrade
    rdf-schema#label	Grade1
    sms:required	sms:false
    rdf-schema#comment	TBD
    isPartOf	http://schema.biothings.io
    sms:displayName	Grade 1


So the working hypothesis is:

Properties - objects of the sms:requiresDependency predicate
Nodes - subjects and objects of the sms:requiresComponent predicate ("components" are Nodes)
Relationships - between Nodes, just use the "requiresComponent" predicate
Terms - objects of the SDO.rangeIncludes predicate
i.e.

    rqcpt_p = uriref('sms:requiresComponent')
    rqdpd_p = uriref('sms:requiresDependency')
    
    nodes = {x for x in g.subject_objects(rqcpt_p)}
    props = {x for x in g.objects(None,rqdpd_p)}
    terms = {x for x in g.objects(None,SDO.rangeIncludes)}

`rdflib.term.URIRef('http://schema.biothings.io/Component')` is a special property. It 
appears to be a tag that holds the category of metadata for the Node. It should therefore
have an acceptable value list (objects of SDO.rangeIncludes), but it does not. It may be
just for submission purposes.

There are just a few Nodes that are internal (are not leaves):

    >>> for node in {x for x in g.objects() if x in g.subjects(rqcpt_p,None) and x in g.objects(None, rqcpt_p)}:
    ...   print(node.split('/')[-1])
    ... 
    RPPALevel2
    ImagingLevel2
    ScRNA-seqLevel1
    ScRNA-seqLevel2
    Biospecimen
    BulkWESLevel2
    ScRNA-seqLevel3
    BulkWESLevel1
    BulkRNA-seqLevel2
    ImagingLevel1
    BulkRNA-seqLevel1
    Patient

(Why include the dash in "-seq" in these identifiers?)

Also, is there overloading of requiresComponent? Looks like there are
vocabulary level groupings that (which combine two attributes: topic
and level) that tag components, but are ancillary to the model logic.
So turn these into two Tags to hang off the actual model entities?

No - it looks like the <disease/tier> entities actually are Nodes that
group Properties that are part the respective tier. The combining of
two atomic attributes in the Node semantics is not ideal.

"Rendering in MDF improves the formal representation of the model by
more precisely specifying the practical function of each entity - "

Fun fact: HTANParticipantID is sprinkled as a Property over 23 Nodes.
Have begun to realize why people (CDIS, DICOM) have separated the data
model from the submission artifacts (e.g. SGTM) in their specs. We do
this as well - MDF and the associated CSVs (which contain the "key"
columns).

Another issue: the jsonld version of the model appears to contain 7139
unique items from the biothings namespace, but nodes, properties and
terms contain 6978 unique items from biothings.  Why the the csv
transformation into jsonld add the extra 161 items?


