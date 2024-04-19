import json
with open('food_services.json', 'r', encoding='utf-8') as file:
    l, res = json.load(file), dict()
    for i in l:
        res.setdefault(i['TypeObject'], {}).setdefault((i['Address'], i['Name']), i["SeatsCount"])
    print(res)
    #for k, v in sorted(res.items()):
    #    mx = max(v.items(), key=lambda x: x[1])
    #    print(f'{k}: {mx[0]}, {mx[1]}')