import random
list1=[]
n=int(input("input elem"))
s=0
for i in range(n):
    element=random.randint(1,10)
    list1.append(element)
    if element>6:
        #element=element
        s+=element*2


for i in list1:
    print(i,end=" ")
print()
print('s=',s)


















































