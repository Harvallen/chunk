import json
with open('countries.json', 'r', encoding='utf-8') as file, open('religion.json', 'w', encoding='utf-8') as rec:
    data = json.load(file)
    result = dict()
    for el in data:
        result.setdefault(el['religion'], []).append(el['country'])
    json.dump(result, rec, indent=3)