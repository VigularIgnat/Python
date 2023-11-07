import random
list1=[]
list2=[]
for i  in range(10):
    elem=random.randint(1,10)
    list2.append(elem)
list2.reverse()
print(list2)
list2.pop(2)
print(list2)
list2.insert(4,"new element")
print(list2)
print(list2.index(max(list2)))
print(list2.count(0))
