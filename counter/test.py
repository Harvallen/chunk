from collections import Counter
def cost(item):
    return sum([ord(char) for char in item if char != ' '])
data = Counter(input().split(','))
for k, v in sorted(data.items()):
    print(f'{k.ljust(len(max(data.keys(), key=len)))}: {cost(k)} UC x {v} = {cost(k) * v} UC')