import requests
import json
from pprint import pprint
from collections import Counter

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
all_heroes = response.json()
heroes = []
heroes_need = ['Hulk', 'Captain America', 'Thanos']
hero_stats = {}
for dict_heroes in all_heroes:
    if dict_heroes.get('name') in heroes_need:
        heroes.append(dict_heroes)
for hero_s in heroes:
    hero_stats.update({hero_s['name']:hero_s['powerstats']['intelligence']})
count = Counter(hero_stats)
sort_count = sorted(count, key=count.get, reverse=True)
print(f'Самый умный супергерой {max(sort_count)}, его интеллект составляет {hero_stats["Thanos"]} у.е.')