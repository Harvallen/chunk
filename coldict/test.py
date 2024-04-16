import json
with open('data1.json', 'r', encoding='utf-8') as file1, open('data2.json', 'r', encoding='utf-8') as file2:
    data1 = json.load(file1)
    data2 = json.load(file2)
    res = data1 | data2

with open('data_merge.json', 'w', encoding='utf-8') as rec:
    json.dump(res, rec)