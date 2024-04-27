import csv, collections
with open('name_log.csv', 'r', encoding='u8') as file:
    [print(f'{t1}: {t2}') for t1, t2 in sorted(collections.Counter([el.strip().split(',')[1] for el in file.readlines()][1:]).most_common())]
    