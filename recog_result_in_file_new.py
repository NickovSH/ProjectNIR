import fileinput
import glob
import os
import re
import wave

import vosk

path_list = ['D:\Универ\НИР\Записи waw\Никита1', 'D:\Универ\НИР\Записи waw\Соня1'
       ]

pattern = '*.txt'


def recognize_vosk():
    # for path in path_list:
    #     for filename in os.listdir(path):
    #         f = os.path.join(path, filename)
    #         if os.path.isfile(f) and filename.endswith('.wav'):
    #             os.system(f'vosk-transcriber -n vosk-model-ru-0.22 -i {f} -o {f}.txt')
    model_path = r"C:\Users\Nikita\.cache\vosk\vosk-model-ru-0.22"

    model = vosk.Model(model_path)
    recognizer = vosk.KaldiRecognizer(model, 16000)

    for i in range(len(path_list)):
        for filename in os.listdir(path_list[i]):
            wf = wave.open(fr"{path_list[i]}/{filename}", "rb")
            data = wf.readframes(240000)
            while data:
                recognizer.AcceptWaveform(data)
                data = wf.readframes(240000)
            result = recognizer.FinalResult()
            # Запись результатов распознавания в файл
            with open(f'{path_list[i]}/{filename}.txt', "w") as f:
                f.write(result)

def deleting_rows():

    for path in path_list:
        glob_path = os.path.join(path, pattern)
        list_files = glob.glob(glob_path)
        for file in list_files:
            with open(file, 'r', encoding='utf-8') as f:
                lines = str(f.readlines())
                # text = lines.replace("{", '').replace('}', '').replace("\\n", '').replace('  "text" : ', '').\
                #     replace('"', '').replace('[', '').replace(']', '').replace("'", '').replace(',', '')
                # # text = text[1: -1]
                text = lines.replace('\\n', ' ')
                text =re.sub("[^А-Яа-я]", " ", lines)
                text = ' '.join(text.split())

            with open(file, 'w', encoding='utf-8') as f:
                f.write(text)

def removing_spaces():
    for path in path_list:
        glob_path = os.path.join(path, pattern)
        list_files = glob.glob(glob_path)
        for file in list_files:
            size = os.path.getsize(file)
            if size == 0:
                with open(file, 'w') as f:
                    f.write('1')

def sort(list_files):
    list_files.sort(key=lambda f: int(re.sub('\D', '', f)))
    return list_files

def results_to_file():
    for path in path_list:
        glob_path = os.path.join(path, pattern)
        list_files = glob.glob(glob_path)
        sort(list_files)
        sort_list_files = list_files
        new_file = f'{path}/result.txt'

        if list_files:
            with fileinput.FileInput(files=list_files, encoding='utf-8') as fr, open(new_file, 'w', encoding='utf-8') as fw:
                for line in fr:
                    # if fr.isfirstline():
                        # file_name = fr.filename()
                        # fw.write(f'\n\n------------ {file_name}\n\n')

                    fw.write(line + '\n')

recognize_vosk()
deleting_rows()
removing_spaces()
results_to_file()