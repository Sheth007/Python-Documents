import re

f=open("Read.txt","r")
i=f.read()
i=re.findall(r'\b\w+\S\w+@\w+.\w+',i)
print(i)
f.close()
