import re

f=open("Read.txt","r")
i=f.read()
i=re.findall(r'[a,e,i,o,u]',i)
print(len(i))
f.close()
    
