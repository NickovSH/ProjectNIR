import fileinput
import glob
import os
import re
import wave

import vosk

path_list = ['D:/Универ/НИР/Phrase_1_8/16/14.10.2013', 'D:/Универ/НИР/Phrase_1_8/16/16.03.2016',
        'D:/Универ/НИР/Phrase_1_8/16/25.09.2013', 'D:/Универ/НИР/Phrase_1_8/27/19.08.2014',
        'D:/Универ/НИР/Phrase_1_8/27/25.07.2014', 'D:/Универ/НИР/Phrase_1_8/27/30.04.2014',
        'D:/Универ/НИР/Phrase_1_8/28/14.07.2014', 'D:/Универ/НИР/Phrase_1_8/28/20.08.2014',
        'D:/Универ/НИР/Phrase_1_8/28/29.07.2014', 'D:/Универ/НИР/Phrase_1_8/30/20.10.2014',
        'D:/Универ/НИР/Phrase_1_8/30/24.09.2014', 'D:/Универ/НИР/Phrase_1_8/30/29.08.2014',
        'D:/Универ/НИР/Phrase_1_8/37/03.04.2015', 'D:/Универ/НИР/Phrase_1_8/37/17.04.2015',
        'D:/Универ/НИР/Phrase_1_8/37/29.02.2016', 'D:/Универ/НИР/Phrase_1_8/44/03.11.2015',
        'D:/Универ/НИР/Phrase_1_8/44/13.11.2015', 'D:/Универ/НИР/Phrase_1_8/44/31.08.2015',
        'D:/Универ/НИР/Phrase_1_8/46/07.10.2015', 'D:/Универ/НИР/Phrase_1_8/46/15.09.2015',
        'D:/Универ/НИР/Phrase_1_8/46/29.09.2015', 'D:/Универ/НИР/Phrase_1_8/48/04.03.2016',
        'D:/Универ/НИР/Phrase_1_8/48/14.01.2016', 'D:/Универ/НИР/Phrase_1_8/48/29.01.2016',
        'D:/Универ/НИР/Phrase_1_8/54/05.05.2016', 'D:/Универ/НИР/Phrase_1_8/54/19.01.2017',
        'D:/Универ/НИР/Phrase_1_8/54/21.03.2016', 'D:/Универ/НИР/Phrase_1_8/56/21.03.2016',
        'D:/Универ/НИР/Phrase_1_8/56/27.04.2016', 'D:/Универ/НИР/Phrase_1_8/59/05.05.2016',
        'D:/Универ/НИР/Phrase_1_8/59/11.04.2016', 'D:/Универ/НИР/Phrase_1_8/59/12.05.2016',
        'D:/Универ/НИР/Phrase_1_8/62/09.09.2016', 'D:/Универ/НИР/Phrase_1_8/62/17.05.2016',
        'D:/Универ/НИР/Phrase_1_8/62/27.04.2016', 'D:/Универ/НИР/Phrase_1_8/65/09.08.2016',
        'D:/Универ/НИР/Phrase_1_8/65/12.08.2016', 'D:/Универ/НИР/Phrase_1_8/65/26.07.2016',
        'D:/Универ/НИР/Phrase_1_8/68/14.09.2016', 'D:/Универ/НИР/Phrase_1_8/68/18.01.2017',
        'D:/Универ/НИР/Phrase_1_8/68/22.08.2016', 'D:/Универ/НИР/Phrase_1_8/68/30.11.2016',
        'D:/Универ/НИР/Phrase_1_8/69/07.10.2016', 'D:/Универ/НИР/Phrase_1_8/69/12.09.2016',
        'D:/Универ/НИР/Phrase_1_8/71/11.10.2016', 'D:/Универ/НИР/Phrase_1_8/71/12.12.2016',
        'D:/Универ/НИР/Phrase_1_8/71/28.03.2017', 'D:/Универ/НИР/Phrase_1_8/71/29.11.2016',
        'D:/Универ/НИР/Phrase_1_8/72/27.10.2016', 'D:/Универ/НИР/Phrase_1_8/72/29.11.2016',
        'D:/Универ/НИР/Phrase_1_8/74/16.12.2016', 'D:/Универ/НИР/Phrase_1_8/74/23.11.2016',
        'D:/Универ/НИР/Phrase_1_8/75/19.12.2016', 'D:/Универ/НИР/Phrase_1_8/75/31.10.2017',
        'D:/Универ/НИР/Phrase_1_8/77/06.02.2017', 'D:/Универ/НИР/Phrase_1_8/77/16.02.2017',
        'D:/Универ/НИР/Phrase_1_8/77/18.01.2017', 'D:/Универ/НИР/Phrase_1_8/77/22.02.2017',
        'D:/Универ/НИР/Phrase_1_8/78/06.04.2017', 'D:/Универ/НИР/Phrase_1_8/78/20.03.2017']

pattern = '*.txt'


def recognize_vosk():
    #Данный вариант скачивает модель при каждом запуске, очень долго ждать результата
    # for path in path_list:
    #     for filename in os.listdir(path):
    #         f = os.path.join(path, filename)
    #         if os.path.isfile(f) and filename.endswith('.wav'):
    #             os.system(f'vosk-transcriber -n vosk-model-ru-0.22 -i {f} -o {f}.txt')

    # Загрузка модели локально, модель инициализируется при каждом запуске цикла, ускоряет работу
    model_path = r"C:\Users\Nikita\.cache\vosk\vosk-model-ru-0.22"


    model = vosk.Model(model_path)
    recognizer = vosk.KaldiRecognizer(model, 16000)

    for i in range(len(path_list)):
        #Проходим циклом по всем указанным путям
        for filename in os.listdir(path_list[i]):
            #Проходим по всем файлам в пути
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

# recognize_vosk()
# deleting_rows()
# removing_spaces()
#results_to_file()