def  print_full_information(*list1):
    for i in list1:
        print("Your order")
        print(i, end=",")

parts=[]
print("Its our restorant order your ingredients ")
while True:
    ingredient=input("Write ingredient")
    if ingredient=="end":
        print_full_information(*parts)
        break
    else:
        parts.append(ingredient)
    
