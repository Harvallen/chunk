import csv
with open('prices.csv', 'r', encoding='utf-8') as file:
    data = csv.reader(file, delimiter=';')
    base = list(zip(*data))
    title, prices = base[0], base[1:]
    result = list()
    min_price_per_row = [min(map(lambda x: int(x), row[1:])) for row in prices]
    min_price_absolute = min(min_price_per_row)
    for product, *price in base:
        if str(min_price_absolute) in price:
            result.append([product, title[price.index(str(min_price_absolute)) + 1]])
    print(': '.join(min(result, key=lambda x: (x[0], x[1])))) 