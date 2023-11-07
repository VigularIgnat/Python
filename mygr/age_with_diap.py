import random
list1=[]

for i in range(0,101):
    if 21<i<79:
        continue
    list1.append(i)
print(list1)
   
    
num=random.randint(0, (len(list1)-1))
list1[num]='end'
print(list1)

for i in list1:
    list1[i]=str(list[i])
    if list1[i]=="end":
        break
    else:
        print(list1[i])
   
    


