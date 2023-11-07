list1=[]
list2=[]
list3=[]
for i in range(10):
    num=int(input("enter number"))
    if num%2==0:
        list1.append(num)
    else:
        list3.append(num)
        if num%5==0:
            list2.append(num)
                
print(list1)
print(list2)
print(list3)
