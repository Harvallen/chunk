import sys
data = tuple(map(int, sys.stdin))
if len(set([data[i + 1] - data[i] for i in range(len(data) - 1)])) == 1:
    print("Арифметическая прогрессия")
elif len(set([data[i + 1] / data[i] for i in range(len(data) - 1)])) == 1:
    print("Геометрическая прогрессия")
else:
    print("Не прогрессия")