import pandas as pd
df=pd.read_csv("wedata.csv")
print(df.columns)
print(df.size)
print(df.info())
print(df.count())
print(df.describe())