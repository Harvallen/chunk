from zipfile import ZipFile
import os
with ZipFile('workbook.zip', 'r') as zip:
    data = zip.infolist()
    print(os.path.basename(max(data, key=lambda x: (x.file_size / x.compress_size) * 100 if not x.is_dir() else 0).filename))