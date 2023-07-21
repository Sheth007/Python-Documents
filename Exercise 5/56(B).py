import pandas as pd
df=pd.read_excel("weekdata.xlsx")

#print(df)
print(df[1::2])