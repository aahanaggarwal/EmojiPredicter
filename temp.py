import pandas as pd

df = pd.read_csv('py_dev_clean.csv')

# list most frequent values in 'emoji' column
print(df['emoji'].value_counts().head(20))