import logging
import rdflib
import skos
import json

logging.basicConfig(level=logging.DEBUG)

with open('OSHA-MultilingualThesaurus.skos', 'r') as file:
    xml = file.read()
graph = rdflib.Graph()
graph.parse(data=xml, format="application/rdf+xml")
loader = skos.RDFLoader(graph)
loader.flat = True

from rdflib.serializer import Serializer
context = {"@OSHA": "http://osha.europa.eu/OSHThesaurus/", "@skos": "http://www.w3.org/2004/02/skos/core#"}
json = graph.serialize(format='json-ld', context=context, indent=2)
with open('OSHA-MultilingualThesaurus.json', 'w') as file:
    file.write(json)
