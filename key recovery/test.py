import json
with open('people.json', 'r', encoding='utf-8') as data, open('updated_people.json', 'w', encoding='utf-8') as rec:
    data = json.load(data)
    keys = dict()
    res = []
    for el in data:
        keys.update(el)
    for k, v in keys.items():
        keys[k] = None
    for el in data:
        r = keys | el
        res.append(r)
    json.dump(res, rec, indent=3)