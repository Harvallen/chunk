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
    with zip.open(names[4]) as file:
        s = file.read().decode('utf-8')
        print(s)