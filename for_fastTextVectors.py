import pandas as pd

df = pd.read_csv('py_dev_clean.csv')

output = open('py_dev_clean_fastText.txt', 'w+')

for index, row in df.iterrows():
    if type(row['sentence']) == float:
        continue
    output.write(row['sentence'] + " " + row['emoji'] + '\n')

output.close()