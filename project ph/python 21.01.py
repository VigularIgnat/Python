import random
n=int(input("write number"))
list1=[]
list2=[]
for i in range(n):
      elem=random.randint(1,100)
      list1.append(elem)
for i in range(n):
      ele=random.random()*1000
      list2.append(ele)
for i in list1:
    print(i, end=" ")
for i in list2:
    print(i, end=" ")
def func_id(number):
    print(list1[number])
def pr(some_list):
    print(sum(some_list))
pr(list1)
p=int(input("input num"))
func_id(p)

