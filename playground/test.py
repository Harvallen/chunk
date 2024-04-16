import csv, json
with open('playgrounds.csv', 'r', encoding='utf-8') as file, open('addresses.json', 'w', encoding='utf-8') as rec:
    data = list(csv.reader(file, delimiter=';'))
    del data[0]
    result = dict()
    for ObjectName, AdmArea, District, Address in data:
        result[AdmArea] = result.setdefault(AdmArea, {})      # переделать в список всех адресов в этом районе.
        result[AdmArea].setdefault(District, []).append(Address)
    json.dump(result, rec, indent=3, ensure_ascii=False)
    