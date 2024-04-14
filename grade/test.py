import csv
with open('student_counts.csv', 'r', encoding='utf-8') as file, open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as output:
    rows = csv.reader(file)
    cols = list(zip(*rows))
    print(cols)
    years, classes = cols[0], cols[1:]
    classes = [years] + sorted(classes, key=lambda x: (int(x[0].split('-')[0]), x[0].split('-')[1]))
    rows = list(zip(*classes))
    w = csv.writer(output)
    w.writerows(rows)