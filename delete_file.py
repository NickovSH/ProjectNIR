from pathlib import Path
path_list = ['D:/Универ/НИР/Phrase_1_8/16/14.10.2013', 'D:/Универ/НИР/Phrase_1_8/16/16.03.2016',
        'D:/Универ/НИР/Phrase_1_8/27/25.07.2014', 'D:/Универ/НИР/Phrase_1_8/27/30.04.2014',
        'D:/Универ/НИР/Phrase_1_8/28/14.07.2014', 'D:/Универ/НИР/Phrase_1_8/28/20.08.2014',
        'D:/Универ/НИР/Phrase_1_8/28/29.07.2014', 'D:/Универ/НИР/Phrase_1_8/30/20.10.2014',
        'D:/Универ/НИР/Phrase_1_8/37/03.04.2015', 'D:/Универ/НИР/Phrase_1_8/37/17.04.2015',
        'D:/Универ/НИР/Phrase_1_8/37/29.02.2016', 'D:/Универ/НИР/Phrase_1_8/44/03.11.2015',
        'D:/Универ/НИР/Phrase_1_8/44/31.08.2015',
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


path = Path(r'D:\Универ\НИР\Phrase_1_8')
for file_name in path.rglob('levenstein.txt'):
    file_name.unlink()