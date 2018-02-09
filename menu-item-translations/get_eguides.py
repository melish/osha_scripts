import json
from bs4 import BeautifulSoup
import urllib2
from collections import defaultdict

BASE_URL = 'https://www.healthy-workplaces.eu/'
LANGUAGES = ['en', 'da', 'de', 'et', 'es', 'fr', 'hr', 'it', 'lv', 'lt', 'hu', 'mt', 'nl', 'no', 'pl', 'pt', 'ro', 'sk', 'sl', 'fi', 'sv', 'is', 'cs', 'el', 'bg']
#LANGUAGES.remove('en')
#LANGUAGES = ['ro',]
PATH = '/tools-and-resources/a-guide-to-psychosocial-risks'

results = dict()

for language in LANGUAGES:
  URL = BASE_URL + language + PATH
  response = urllib2.urlopen(URL)
  html = response.read()
  parsed_html = BeautifulSoup(html)
  h2 = parsed_html.body.find('h2', attrs={'id':'eguides_filter_intro'})
  results[language] = h2.text.strip()

with open('online_download_translation.json', 'r') as f:
  origdata = json.loads(f.read())
for obj in origdata:
    obj['text2'] = results[obj['language']]
jsonfile = open('translations.json', 'w')
jsonfile.write(json.dumps( origdata,  sort_keys=False, indent=2))

