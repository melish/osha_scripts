import csv
import json
from StringIO import StringIO
import sys

content = open(sys.argv[1], 'r')
jsonfile = open(sys.argv[1] + '.json', 'w')
reader = csv.DictReader( content, quotechar='"', delimiter=';', escapechar='\\')
out=[]
try:
    for row in reader:
        out.append(row)
except Exception  as e:
    print e
    print '*** Error parsing after line:'
    print out[-1]
jsonfile.write(json.dumps( out,  sort_keys=True, indent=2))
