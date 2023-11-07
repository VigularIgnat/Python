import random
mas=[]

n=int(input("enter number of elem"))
for i in range(n):
    elem=random.randint(1,100)
    mas.append(elem)
    if elem%2==0:
        print(elem)
        

for i in mas:
    print(i, end=" ")
    
