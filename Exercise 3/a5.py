import re

f=open("Read.txt","r")
i=f.read()
i=re.findall(r'\b\w{5}\b',i)
print(i)
f.close()
