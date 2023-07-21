import re
f=open("Read.txt","r")
i=f.read()
i=re.findall("s\w+",i)
print(i)
f.close()

