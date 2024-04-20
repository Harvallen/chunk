from zipfile import ZipFile
def size_coverter(size):
    count = 0
    d = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB'}
    while size / 1024 > 1:    
        size /= 1024
        count += 1
    return f'{round(size)} {d[count]}'
with ZipFile('desktop.zip') as file:
    data = file.infolist()
    for el in data:
        seq = list(filter(lambda x: x != '' ,el.filename.split('/')))
        if el.is_dir():
            print(f"{'  ' * (len(seq) - 1)}{seq[-1]}")
        else:
            print(f"{'  ' * (len(seq) - 1)}{seq[-1]} {size_coverter(el.file_size)}")