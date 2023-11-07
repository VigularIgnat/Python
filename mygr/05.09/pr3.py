list1=["Roma","Oleg", "Vanya", "Artem"]


for elem in list1:
    f=len(list1)
    if f>=1:
        element=list1.pop()
        print(list1, element)
        
        print(f"I so soryy {elem}")
    else:
        break
        
print(list1)
