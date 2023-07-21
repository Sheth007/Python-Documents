import pandas as pd
df=pd.read_excel("weekdata.xlsx")

ndf=df.dropna(axis=1)
print(ndf)