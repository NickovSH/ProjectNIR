import scipy.stats as stats
import pandas

head = ['model-ru-0.10', 'model-ru-0.10-lgraph', 'model-ru-0.22', 'model-ru-0.42',	'model-small-ru-0.15',
        'model-small-ru-0.22', 'model-small-ru-0.3', 'model-small-ru-0.4', 'Kaldi-ru-0,7']
pvalue = []
excel_data_df = pandas.read_excel(r'D:\Универ\НИР\Второй семак\result.xlsx', sheet_name='1')

for i in head:
    group1 = excel_data_df[i].tolist()
    for n in head:
        if i != n:
            group2 = excel_data_df[n].tolist()
            print(i, n, stats.wilcoxon(group1, group2))
        else:
            continue

print(pvalue)
