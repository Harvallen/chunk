from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as file:
    data = pickle.load(file)
    for el in data:
        beast = el
        for field, value in zip(Animal._fields, beast):
            print(f'{field}: {value}')
        print()