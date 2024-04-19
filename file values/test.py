from zipfile import ZipFile
with ZipFile('workbook.zip','r') as zip:
    data = zip.infolist()
    print(f'Объем исходных файлов: {sum(map(lambda x: x.file_size, data))} байт(а)')
    print(f'Объем сжатых файлов: {sum(map(lambda x: x.compress_size, data))} байт(а)')