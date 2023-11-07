from tkinter import *
from math  import sqrt
def add():
    a= int(input("Увести a: "))
    b= int(input("Увести b: "))
    print("add=", a+b)
def product():
    a= int(input("Введіть a: "))
    b= int(input("Введіть b: "))
    print("product=", a*b)
def minus():
    a= int(input("Введіть a: "))
    b= int(input("Введіть b: "))
    print("product=", a-b)
def koring():
    n=int(input("n="))
    number= sqrt(n)
    print("koring=", number)
root=Tk()
but1=Button(root)
but1=Button(root, text="додавання", width= 15, height=2, bg="blue",
            fg="white", command= add)
but2=Button(root)
but2=Button(root, text= "Множення", width= 30, height=3, bg ="yellow",
            fg="red", command= product)
but3=Button(root)
but3=Button(root, text= "Віднімання", width= 30, height=3, bg ="purple",fg="white", command= minus)

but4=Button(root)
but4=Button(root, text="корінь", width= 15, height=3, bg="green", fg="black", command= koring)
but1.pack()
but2.pack()
but3.pack()
but4.pack()
root.mainloop()
