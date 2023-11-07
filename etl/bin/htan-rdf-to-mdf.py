import re
from bento_mdf.mdf import MDF
from bento_meta.model import Model
from bento_meta.objects import Node, Edge, Property, Term, ValueSet
from rdflib import Graph
from rdflib.namespace import Namespace, NamespaceManager
from rdflib.term import URIRef
from rdflib.namespace import RDF, RDFS, SDO

from pdb import set_trace

htan_ld = "HTAN.model.jsonld"
g = Graph().parse(file= open(htan_ld))
nms = NamespaceManager(g)
BTS = Namespace(nms.expand_curie('bts:'))
SMS = Namespace('sms:')


qe = lambda x:re.sub("(\w)'(\w)",r"\1''\2",x)

def get_atts(ent: URIRef, g: Graph):
    atts = {
        "label": qe(str(g.value(ent, RDFS.label, None))),
        "comment": qe(str(g.value(ent, RDFS.comment, None))),
        "displayName": qe(str(g.value(ent, SMS.displayName, None))),
    }
    
    return atts
    

ht_nodes = {x for x in g.subjects(SMS.requiresComponent, None)}.union(
    {x for x in g.objects(None, SMS.requiresComponent)})
ht_props = {x for x in g.objects(None, SMS.requiresDependency)}
ht_terms = {x for x in g.objects(None, SDO.rangeIncludes)}

model = Model(handle="HTAN")

for nd in ht_nodes:
    # get rdf info
    atts = get_atts(nd, g)
    node = model.add_node({"handle": atts["label"], "desc": atts["comment"]})
    model.annotate(node, Term({"value": atts["displayName"],
                               "origin_name": "HTAN",
                               "origin_id": str(nd)}))
    # collect properties
    prs = g.objects(nd, SMS.requiresDependency, unique=True)
    for pr in prs:
        patts = get_atts(pr, g)
        prop = model.add_prop(node, Property({"handle": patts["label"],
                                         "desc": patts["comment"]}))
        model.annotate(prop, Term({"value": patts["displayName"],
                                   "origin_name": "HTAN",
                                   "origin_id": qe(str(pr))}))
        vals = list(g.objects(pr, SDO.rangeIncludes, unique=True))
        if vals:
            prop.value_domain = "value_set"
            for vl in vals:
                vatts = get_atts(vl, g)
                model.add_terms(prop, Term({"value": vatts["displayName"],
                                            "origin_name": "HTAN",
                                            "origin_id": qe(str(vl)),
                                            "origin_definition": vatts["comment"]}))
            pass
        else:
            pr.value_domain = "TBD"
# edges
for dst in g.objects(None,SMS.requiresComponent,unique=True):
    datts = get_atts(dst, g)
    for src in g.subjects(SMS.requiresComponent,dst, unique=True):
        satts = get_atts(src, g)
        model.add_edge(Edge({"handle": "requires_component",
                             "src": model.nodes[satts["label"]],
                             "dst": model.nodes[datts["label"]]}))


mdf = MDF(model=model)
mdf.write_mdf(file="htan-model.yaml")
pass
