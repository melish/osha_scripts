import json
from bs4 import BeautifulSoup
import urllib2
from collections import defaultdict

BASE_URL = 'http://osha.europa.eu/'
PATH = '/contact_us_form'
LANGUAGES = ['en', 'da', 'de', 'et', 'es', 'fr', 'hr', 'it', 'lv', 'lt', 'hu', 'mt', 'nl', 'no', 'pl', 'pt', 'ro', 'sk', 'sl', 'fi', 'sv', 'is', 'cs', 'el', 'bg']
#LANGUAGES = ['en', 'ro',]

results = dict()

for language in LANGUAGES:
  URL = BASE_URL + language + PATH
  response = urllib2.urlopen(URL)
  html = response.read()
  parsed_html = BeautifulSoup(html)
  select = parsed_html.body.find('select', attrs={'id':'subject'})
  for i, option in enumerate(select.findAll('option')):
    key = option['value']
    if not key in results:
        results[key] = {}
    results[key][language] = option.text
jsonfile = open('subjects.json', 'w')
jsonfile.write(json.dumps( results,  sort_keys=False, indent=2))

