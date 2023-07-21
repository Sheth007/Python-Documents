import pandas as pd
df=pd.read_excel("weekdata.xlsx")

print(df["CallingNumber"][df["DayOfWeek"] == "mon"])