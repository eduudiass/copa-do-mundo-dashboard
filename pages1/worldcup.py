import pandas as pd

df = pd.read_csv('worldcup.csv', enconding='latin1')
print(df.head())
print(df.info())
