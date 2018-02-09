import csv
import json
from StringIO import StringIO

content = open('case_studies_aliases.txt', 'r')
jsonfile = open('case_studies_aliases.json', 'w')
reader = csv.DictReader( content, quotechar='"', delimiter=';', escapechar='\\')
out=[]

for row in reader:
    row['filename'] = row['filename'].split('/')[-1]
    out.append(row)

print "Total rows: %d\n" % len(out)
jsonfile.write(json.dumps( out,  sort_keys=True, indent=2))

