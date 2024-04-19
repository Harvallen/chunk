from zipfile import ZipFile
import json

def is_correct_json(string):
    try:
        json_data = json.loads(string)
        return True
    except:
        return False
    
with ZipFile('data.zip') as zip:
    names = zip.infolist()
    foot = list()
    for el in names:
        with zip.open(el) as z:
            try:
                json_data = json.loads(z.read().decode('utf-8'))
                foot.append(json_data)    
            except:
                continue
    [print(el['first_name'], el['last_name']) for el in sorted(filter(lambda x: x['team'] == 'Arsenal', foot), key=lambda q: (q['first_name'], q['last_name']))]