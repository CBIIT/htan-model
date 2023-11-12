#!/usr/bin/env python
import re
import argparse
import yaml
import json
import tempfile
# from pdb import set_trace
from bento_mdf.mdf import MDF
from bento_meta.model import Model
from bento_meta.objects import Node, Edge, Property, Term, ValueSet
from rdflib import Graph
from rdflib.namespace import Namespace, NamespaceManager
from rdflib.term import URIRef
from rdflib.namespace import RDF, RDFS, SDO
from urllib.parse import quote

parser = argparse.ArgumentParser(description="Convert HTAN JSON-LD model to MDF")
parser.add_argument('infile', nargs=1, metavar="JSONLD-file", help="JSON-LD model file")
args = parser.parse_args()
print(args.infile)
htan_ld = args.infile[0]  # "HTAN.model.jsonld"

jsn = json.load(open(htan_ld,"r"))

# hack HTAN jsonld so rdflib can work
# remove the top-level graph @id
del jsn["@id"]
# change SDO namespace URI from http to https
jsn["@context"]["schema"] = "https://schema.org/"

tmp = tempfile.NamedTemporaryFile(mode="w+")
# remove special chars from URIs

for l in json.dumps(jsn,indent=2).split(sep="\n"):
    if re.match(".*bts:",l):
        l = l.replace('<','_lt_')
        l = l.replace('>','_gt_')
        l = l.replace('=','_eq_')
        l = l.replace('^','_up_')
    print(l, file=tmp)
tmp.seek(0)


g = Graph().parse(file= tmp.file, format="json-ld", publicID="http://schema.biothings.io/#0.1")
nms = NamespaceManager(g)
BTS = Namespace(nms.expand_curie('bts:'))
SMS = Namespace('sms:')


def qe(x):
    ''' Escape apostrophes '''
    return re.sub("(\w)'(\w)",r"\1''\2",x)


def norm_hdl(x):
    hdl = re.sub("[']","",x)
    hdl = re.sub("^([0-9])","_\\1",hdl)
    hdl = re.sub("[ -./!@#$%&*()?+=]","_",hdl)
    return hdl
    

def get_atts(ent: URIRef, g: Graph):
    atts = {
        "label": qe(str(g.value(ent, RDFS.label, None))),
        "comment": qe(str(g.value(ent, RDFS.comment, None))) or  "None provided",
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
    node = model.add_node({"handle": norm_hdl(atts["label"]),
                           "desc": atts["comment"]})
    model.annotate(node, Term({"value": atts["displayName"],
                               "origin_name": "HTAN",
                               "origin_id": str(nd),
                               "origin_definition": atts["comment"],
                               "handle": norm_hdl(atts["displayName"])}))

    # collect properties
    prs = g.objects(nd, SMS.requiresDependency, unique=True)
    for pr in prs:
        patts = get_atts(pr, g)
        prop = model.add_prop(node, Property({"handle": norm_hdl(patts["label"]),
                                              "desc": patts["comment"]}))
        model.annotate(prop, Term({"value": patts["displayName"],
                                   "origin_name": "HTAN",
                                   "origin_id": qe(str(pr)),
                                   "origin_definition": patts["comment"],
                                   "handle": norm_hdl(patts["displayName"])}))
        vals = list(g.objects(pr, SDO.rangeIncludes, unique=True))
        if vals:
            prop.value_domain = "value_set"
            for vl in vals:
                vatts = get_atts(vl, g)
                model.add_terms(prop, Term({"value": vatts["displayName"],
                                            "origin_name": "HTAN",
                                            "origin_id": qe(str(vl)),
                                            "handle": norm_hdl(vatts["displayName"]),
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
                             "multiplicity": "one_to_many",
                             "src": model.nodes[norm_hdl(satts["label"])],
                             "dst": model.nodes[norm_hdl(datts["label"])]}))


mdf = MDF(model=model)
mdf_dict = mdf.write_mdf()

# kludge - need fix in bento-mdf
mdf_dict["Relationships"]['requires_component']['Props'] = None
with open("htan-model.yaml","w") as f:
    yaml.dump({k:mdf_dict[k] for k in mdf_dict if k in
               ["Handle", "Nodes", "Relationships"]}, stream=f,
              indent=4)

with open("htan-model-props.yaml","w") as f:
    yaml.dump({k:mdf_dict[k] for k in mdf_dict if k in
               ["PropDefinitions"]}, stream=f,
              indent=4)

with open("htan-model-terms.yaml","w") as f:
    yaml.dump({k:mdf_dict[k] for k in mdf_dict if k in ["Terms"]},
              stream=f, indent=4)
                       

