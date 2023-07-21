import pandas as pd
df=pd.read_excel("weekdata.xlsx")

df.dropna(inplace=True)
print(df)