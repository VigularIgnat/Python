#програма Логічні величини і вирази
#вхідні дані: x, y, z
#обробка присвоювання логічних величин з виразу
#Костенко Іван, 7г

x=int(input("Введіть x "))
y=int(input("Введіть y "))
z=int(input("Введіть z "))
condition=((x>0) and (y>0) and (z>0))
condition2=((x>0) or (y>0) or (z>0))
if ((x>=5) and (x<=10)):
    a=True
if (x%2==0):
    a=True
if ((x>y) and (x%2==0)):
    a=True