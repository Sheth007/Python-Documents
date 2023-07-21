f=open("u.txt","r")
data=f.read()
count=0
for i in data:
    count+=1
print(count)
f.close()
