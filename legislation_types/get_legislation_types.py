import json
from bs4 import BeautifulSoup
import urllib2
from collections import defaultdict

BASE_URL = 'http://osha.europa.eu/'
PATH = '/legislation/directives'
LANGUAGES = ['da', 'de', 'et', 'en', 'es', 'fr', 'hr', 'it', 'lv', 'lt', 'hu', 'mt', 'nl', 'no', 'pl', 'pt', 'ro', 'sk', 'sl', 'fi', 'sv', 'is', 'cs', 'el', 'bg']
URL_PREFIX = '/en/legislation/directives/'

categories = [{}, {}, {}, {}, {}, {}, {}]

for language in LANGUAGES:
  URL = BASE_URL + language + PATH
  response = urllib2.urlopen(URL)
  html = response.read()
  parsed_html = BeautifulSoup(html)
  categ_div = parsed_html.body.find('div', attrs={'class':'boxing_styles_content'})
  for i, categ_link in enumerate(categ_div.findAll('a', href=True)):
    text = categ_link.find('strong').text.strip()
    code = categ_link['href'][len(URL_PREFIX):].replace('/', '')
    categories[i][language] = text
    categories[i]['code'] = code

jsonfile = open('legislation.json', 'w')
jsonfile.write(json.dumps( categories,  sort_keys=False, indent=2))

