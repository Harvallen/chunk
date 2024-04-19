from zipfile import ZipFile
import datetime
with ZipFile('workbook.zip', 'r') as file:
    data = file.infolist()
    for el in filter(lambda x: not x.is_dir(), sorted(data, key=lambda x: x.filename.split('/')[-1])):
        print(el.filename.split('/')[-1])
        print(f'  Дата модификации файла: {datetime.datetime(*el.date_time)}')
        print(f'  Объем исходного файла: {el.file_size} байт(а)')
        print(f'  Объем сжатого файла: {el.compress_size} байт(а)')
        print()