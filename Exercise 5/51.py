import pandas as pd 
data={"id":[1,2,3,4,5],"name":["abc","def","ghi","jkl","mno"],"city":["rajkot","rajkot","rajkot","rajkot","rajkot"],"Department":["csit","csit","csit","csit","csit"], "Designation":["profesir","profesir","profesir","profesir","profesir"], "Salary":["50000","50000","50000","50000","50000"]}
df = pd.DataFrame(data)
print(df)