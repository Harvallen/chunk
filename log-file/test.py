import csv, datetime

with open('name_log.csv', 'r', encoding='utf-8') as file, open('new_name_log.csv', 'w', encoding='utf-8') as rec:
    data = list(csv.reader(file))
    del data[0]
    result = dict()
    for el in sorted(data, key=lambda x: datetime.datetime.strptime(x[-1], '%d/%m/%Y %H:%M')):                         #   sorted by datetime
        username, email, dt = el
        result[email] = (username, dt)
    print(f'username,email,dtime', file=rec)
    [print(f'{v[0]},{k},{v[1]}', file=rec) for k, v in sorted(result.items())]                                         #   sorted by keys