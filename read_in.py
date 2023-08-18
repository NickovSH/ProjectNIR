import fileinput
import os
import glob
import pathlib

path = 'D:/Универ/НИР/Phrase/16/14.10.2013'
pattern = '*.txt'

glob_path = os.path.join(path, pattern)
list_files = glob.glob(glob_path)
# расширение нового файла установим как '.all'
new_file = 'new_file.doc'

if list_files:
    # открываем список файлов 'list_files' на чтение
    # и новый общий файл 'new_file' на запись
    with fileinput.FileInput(files=list_files) as fr, open(new_file, 'w') as fw:
        # читаем данные построчно
        for line in fr:
            # определяем первую строку нового файла
            if fr.isfirstline():
                # название читаемого файла
                file_name = fr.filename()
                # дописываем строку с названием файла
                fw.write(f'\n\n------------ {file_name}\n\n')

            fw.write(line)