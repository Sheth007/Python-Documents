def circle(r):
    return 3.14*r*r

def rect(l,b):
    return l*b;

def tria(b,h):
    return 0.5*b*h

r=int(input("Enter a number :"))
area=circle(r)
print(area)

l=int(input("Enetr a vlue :"))
b=int(input("Enetr a vlue :"))
area=rect(l,b)
print(area)

b=int(input("Enetr a vlue :"))
h=int(input("Enetr a vlue :"))
area=rect(b,h)
print(area)