import csv
import json
from StringIO import StringIO
import sys
import traceback

content = open(sys.argv[1], 'r')
jsonfile = open(sys.argv[1] + '.json', 'w')
reader = csv.DictReader( content, quotechar='"', delimiter=';', escapechar='\\')
out=[]
extra_field_names=['description', 'info', 'canonical', 'country', 'workflow_state', 'nace', 'imageCaption', 'subject', 'subcategory', 'multilingual_thesaurus', 'location',  'notesToEditors',  'relatedLinks',  'releaseDate',  'releaseTiming',  'subhead', 'attachment',  'attendees',  'contactEmail',  'contactName',  'contactPhone',  'dateToBeConfirmed',  'startDate',  'endDate',  'eventUrl',  'location', 'author', 'shortlisted', 'relatedItems', 'file', 'files', 'image', 'language', 'publication_date', 'path', 'title', 'archived', 'expiration_date']
extra_fields={}
for field in extra_field_names:
    extra_fields[field] = set()
unique_items=set()

try:
    for row in reader:
        out.append(row)
        for field in extra_field_names:
            if row.get(field):
                extra_fields[field].add(row.get(field))
        if ( row['workflow_state'] in ['published', 'checked', 'to_amend']):
            if ( row.get('canonical') ):
                unique_items.add(row['canonical'])
            else:
                unique_items.add(row['path'])
        
except Exception as e:
    print traceback.format_exc()
    print e
    print '*** Error parsing after line:'
    print out[-1]
print "Total rows: %d\n" % len(out)
jsonfile.write(json.dumps( out,  sort_keys=True, indent=2))

for field in extra_field_names:
    with open(sys.argv[1] + '.' + field, 'w') as f:
        f.write("\n".join(extra_fields[field]))
with open(sys.argv[1] + '.path-canonical', 'w') as f:
    f.write("\n".join(unique_items))
