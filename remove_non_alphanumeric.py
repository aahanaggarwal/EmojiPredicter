import pandas as pd
import re

df = pd.read_csv('py_dev.csv')

for index, row in df.iterrows():
    df.loc[index, 'sentence'] = re.sub(r'[^a-zA-Z0-9 ]', '', row['sentence']).strip()

pd.DataFrame.to_csv(df, 'py_dev_clean.csv', index=False)