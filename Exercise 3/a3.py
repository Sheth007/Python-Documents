import re

f=open("Read.txt","r")
i=f.read()
i=re.findall(r"\d{2}/\d{2}/\d{4}",i)
print(i)
f.close()
