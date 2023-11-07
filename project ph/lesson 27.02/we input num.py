import random
list1=[]
n=int(input("input elem"))
for i in range(n):
    element=int(input('input element'))
    list1.append(element)
list1.pop(1)
print(max(list1))
for i in list1:
    print(i)
sort(list1)

