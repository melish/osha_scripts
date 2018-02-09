import json
from bs4 import BeautifulSoup
import urllib2
from collections import defaultdict

BASE_URL = 'http://www.healthy-workplaces.eu/'
LANGUAGES = ['en', 'da', 'de', 'et', 'es', 'fr', 'hr', 'it', 'lv', 'lt', 'hu', 'mt', 'nl', 'no', 'pl', 'pt', 'ro', 'sk', 'sl', 'fi', 'sv', 'is', 'cs', 'el', 'bg']
LANGUAGES.remove('en')
#LANGUAGES = ['en', 'ro',]

results = dict()

for language in LANGUAGES:
  URL = BASE_URL + language
  response = urllib2.urlopen(URL)
  html = response.read()
  parsed_html = BeautifulSoup(html)
  menu = parsed_html.body.find('li', attrs={'id':'portaltab-media-centre'})
  menuitem = menu.find('ul', attrs={'class':'submenu dropdown-menu'})
  li = menuitem.findAll('li')[5]
  results['edit-translations-'+language] = li.a.text.strip()

jsonfile = open('translations.json', 'w')
jsonfile.write(json.dumps( results,  sort_keys=False, indent=2))

