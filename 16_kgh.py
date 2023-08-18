import os

path_list_input = ['D:\Универ\НИР\waw\Никита', 'D:\Универ\НИР\waw\Соня']
path_list_output = ['D:\Универ\НИР\waw\Никита1', 'D:\Универ\НИР\waw\Соня1']


for i in range(len(path_list_input)):
    # Проходим по указанному пути и меняем частоту дискретизации на 16 кГц
    for filename in os.listdir(path_list_input[i]):
        print(path_list_input[i])
        os.system(fr'ffmpeg -i {path_list_input[i]}/{filename} -ar 16000 {path_list_output[i]}/{filename}.wav')