import csv, json, datetime
with open('exam_results.csv', 'r', encoding='utf-8') as file:
    data = csv.DictReader(file)
    info = dict()
    result = list()
    for el in data:
        name, surname, score, date, email = el.values()
        dt = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        if f'{name} {surname}' not in info:
            info[f'{name} {surname}'] = [score, dt, email]
        elif info[f'{name} {surname}'][0] < score or info[f'{name} {surname}'][0] == score and info[f'{name} {surname}'][1] < dt:
            info[f'{name} {surname}'] = [score, dt, email]
    for name, infos in info.items():
        result.append({"name": name.split()[0], "surname": name.split()[1], "best_score": int(infos[0]), "date_and_time": infos[1].strftime('%Y-%m-%d %H:%M:%S'), "email": infos[2]})
    t = json.dumps(sorted(result, key=lambda x: x['email']), indent=3)
    with open('best.scores.json', 'w', encoding='utf-8') as rec:
        print(t,file=rec)