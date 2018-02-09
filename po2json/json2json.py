import json
from pprint import pprint
from collections import defaultdict

languages = ['bg', 'ca', 'cs', 'da', 'de', 'el', 'en', 'es', 'et', 'fi', 'fr', 'hr', 'hu', 'is', 'it', 'ja', 'lt', 'lv', 'mt', 'nl', 'no', 'pl', 'pt', 'ro', 'ru', 'sk', 'sl', 'sv', 'tr']
#languages = ['ro']

film_meta = {
    'id': 'napo-020-shocking-situations',
    'episodes': [
      'napo-020-shocking-situations-episode-001-push-pull',
      'napo-020-shocking-situations-episode-002-over-and-out',
      'napo-020-shocking-situations-episode-003-positive-charge',
      'napo-020-shocking-situations-episode-004-nearby-accident',
      'napo-020-shocking-situations-episode-005-double-dose',
      'napo-020-shocking-situations-episode-006-in-the-heat-of-the-moment',
      'napo-020-shocking-situations-episode-007-high-risk-intervention',
      'napo-020-shocking-situations-episode-008-lock-out',
      'napo-020-shocking-situations-episode-009-aggravating-factors',
      'napo-020-shocking-situations-episode-010-high-voltage'
    ]
}

film_id = film_meta['id']
out=dict()
out['episodes'] = dict()
for e_id in film_meta['episodes']:
    out['episodes'][e_id] = dict()

for lang in languages:
    print lang
    with open('napo-data/osha-' + lang + '.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        out['description_' + lang] = data.get('description_' + film_id, '')
        out['title_' + lang] = data.get('heading_' + film_id, '')
        for e_id in film_meta['episodes']:
            out['episodes'][e_id]['title_' + lang] = data.get('heading_' + e_id, '')

result = dict()
result[film_id] = out

with open(film_id + '.json', 'w') as jsonfile:
    jsonfile.write(json.dumps( result,  sort_keys=True, indent=2))

