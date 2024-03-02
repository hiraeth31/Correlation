import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('norwKr.xlsx')

df.drop(['nominal', 'cdx'], inplace=True, axis=1)
df['data'] = pd.to_datetime(df['data'])
df.index = df['data']

df['Year'] = df.index.year
df['Month'] = df.index.month
df['Day'] = df.index.day
dates = df[['Year', 'Month', 'Day']]

df.index = pd.MultiIndex.from_tuples(dates.values.tolist(), names=dates.columns)

print(df.head(10))




