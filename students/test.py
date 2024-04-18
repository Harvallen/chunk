import json, csv
with open('students.json', 'r', encoding='utf-8') as file, open('data.csv', 'w', encoding='utf-8') as rec:
    data = json.load(file)
    print('name,phone', file=rec)
    result = list()
    for el in data:
        name, city, age, progress, phone = el.values()
        if age >= 18 and progress >= 75:
            result.append(f'{name},{phone}')
    print(*sorted(result), sep='\n', file=rec)