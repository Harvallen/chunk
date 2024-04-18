import json
with open('food_services.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    distr = dict()
    name = dict()
    for el in data:
        distr[el['District']] = distr.setdefault(el['District'], 0) + 1
        if el['IsNetObject'] == 'да':
            name[el['OperatingCompany']] = name.setdefault(el['OperatingCompany'], 0) + 1
    print(*max(distr.items(), key=lambda x: x[1]), sep=': ')
    print(*max(name.items(), key=lambda x: x[1]), sep=': ')