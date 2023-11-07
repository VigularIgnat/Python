import random
n=int(input("Enter number of element"))
list1=[]
for i in range(n):
    r=int(input("write element"))
    list1.append(r)
    f=sum(list1)
print(f)
d=f/n
print(d)
b=random.randint(1,5)
for i in range(b):
    g=int(input("Enter g"))
    w=int(input("enter w"))
    su=g*w
    list1.append(su)
print(list1)
