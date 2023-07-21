import re

f=open("Read.txt","r")
i=f.read()
i=re.findall(r'\w+.$',i)
print(i)
f.close()
