import pandas as pd 
df=pd.read_csv("wedata.csv")
print(df.sort_values(by="name"))
