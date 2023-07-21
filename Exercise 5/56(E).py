import pandas as pd
df=pd.read_excel("weekdata.xlsx")

#print(df)
a=df[df["CallDuration"] > 10] 
print(a.to_string())