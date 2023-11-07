n=int(input("Введіть n "))
arr1=[6,8,10,12]


if n in arr1:
    from turtle import *
    from random import*
  
    shape('turtle')
    width(3)
    
    colors=['blue','red','yellow','green', 'gray','brown','purple']
    alfa=360/n
    for j in range(n):
        color(colors[randint(0,6)])
        for i in range(4):
            forward(100)
            right(90)
        left(alfa)
else:
    print("Введену неправильну кількість квадратів!")
            
