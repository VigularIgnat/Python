#переставити сусідні елементи списку



import random

mas=[]

number=11

for i in range(number):
    elem=random.randint(1,90)
    mas.append(elem)


print(mas)

for i in range(0,len(mas)-1,2):
    mas[i], mas[i+1]=mas[i+1], mas[i]
    

print(mas)
