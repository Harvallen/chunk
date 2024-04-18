import json, datetime
with open('pools.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    t_day, t_start, t_end = 'Вторник', datetime.time(13), datetime.time(16)
    pools_time_agreed = list()
    for el in data:
        ObjectName, AdmArea, District, Address, WorkingHoursSummer, DimensionsSummer = el.values()
        obj_start_time, obj_end_time = [datetime.time(int(t.split(':')[0]), int(t.split(':')[1])) for t in WorkingHoursSummer[t_day].split('-')]
        if t_start >= obj_start_time and t_end <= obj_end_time:
            pools_time_agreed.append([DimensionsSummer['Length'], DimensionsSummer['Width'], Address])
    result = max(pools_time_agreed, key= lambda x: (x[0], x[1]))
    print(f'{result[0]}x{result[1]}', result[2], sep='\n')