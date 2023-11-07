list1=["Roma","Oleg", "Vanya", "Artem"]

for i in list1:
    print(f"I am inviting you {i} to my party")

list1.insert(0,"Drap")


f=len(list1)
summ=f//2

list1.insert(summ,"Eva")



for elem in list1:
    f=len(list1)
    if f>=1:
        list1.pop(f)
        
        print(f"I so soryy {elem}")
    else:
        break
        
print(list1)


for f in len(list1):
    del list1[f:f+1]
print(list1)
