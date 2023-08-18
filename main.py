import levenstein
import recog_result_in_file

if __name__ == "__main__":
    recog_result_in_file.recognize_vosk()    #Запуск модуля распознавания речи
    recog_result_in_file.deleting_rows()    #Запуск модуля удаления пробелов и всего кроме киррилицы
    #recog_result_in_file.removing_spaces()
    recog_result_in_file.results_to_file()    #Запись в файл результатов распознавания
    levenstein.levenstein()    #Расчет расстояния Левенштейна