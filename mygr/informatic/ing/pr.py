import math

a=int(input(" Введіть a ", ))
b=int(input(" Введіть b ", ))
c=int(input(" Введіть c ", ))

p= (a+b+c)/2

s= math.sqrt((p*(a-b)*(p-b)*(p-c)))
print("Площа трикутника дорівнює ", round(s))
