import csv
def condense_csv(filename, id_name):
    with open(filename, 'r', encoding='utf-8') as data, open('condensed.csv', 'w', encoding='utf-8') as rec:
        text = csv.reader(data)
        result = dict()
        title = list()
        for el in text:
            num, prop, value = el
            result.setdefault(num, {}).update({prop:value})
            if prop not in title:
                title.append(prop)
        print(f"{id_name},{','.join(title)}", file=rec)
        for key, value in result.items():
            print(f'{key},' + ','.join([v for v in value.values()]), file=rec)




condense_csv('data.csv', id_name='ID')