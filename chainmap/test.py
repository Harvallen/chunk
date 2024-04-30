import json
from collections import ChainMap, Counter

with open('zoo.json', 'r', encoding='u8') as file:
    data = json.load(file)
    print(sum(ChainMap(*data).values()))
