import json

with open('data.json', encoding='utf-8') as file, open('updated_data.json', 'w', encoding='utf-8') as new_file:
    data = json.load(file)
    conv_values = {
        str: lambda x: x + '!',
        int: lambda x: x + 1,
        bool: lambda x: not x,
        list: lambda x: x * 2,
        dict: lambda x: {**x, "newkey": None},
    }
    new_data = []
    for d in data:
        if type(d) in conv_values:
            new_data.append(conv_values[type(d)](d))
    json.dump(new_data, new_file, indent=2)