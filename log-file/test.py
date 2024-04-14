import csv, datetime
import os
print("Текущая рабочая директория:", os.getcwd())
with open('name_log.csv', 'r', encoding='utf-8') as file, open('new_name_log.csv', 'w', encoding='utf-8'):
    data = list(csv.reader(file))
    del data[0]
    result = dict()
    for el in sorted(data, key=lambda x: datetime.strptime(x[-1], '%d/%m/%Y %H:%M')):                         #   sorted by datetime
        username, email, dt = el
        result[email] = username