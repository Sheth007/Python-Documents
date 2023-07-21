import re
i=input("Enter a password")
i=re.findall("[A-za-z0-9!@#$%^&*_]{8,22}",i)
if i!=[]:
    print("Pssword Matched")
else:
    print("Password Unmatched")
print(i)
