import pandas as pd
df=pd.read_csv("student.csv")
newdf=df.head(10)
new2df=df.tail(10)
print(newdf.to_string())
print(new2df.to_string())