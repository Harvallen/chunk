from zipfile import ZipFile
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.namelist()
    print(info)