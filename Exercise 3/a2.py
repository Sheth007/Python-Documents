import re
f=open("Read.txt","r")
i=f.read()
i=re.findall(r"\b\d{10}\b",i)
print(i)
f.close()
