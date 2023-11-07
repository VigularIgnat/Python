import random
mas=[]

number=20

for i in range(number):
    elem=random.randint(1,99)
    mas.append(elem)

print(mas)
summ=0
for i in range(2,len(mas)-1,2):
    if mas[i+1]< mas[i]>mas[i-1]:
        summ+=1
        print(mas[i])
print(summ)
