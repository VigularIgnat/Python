from tkinter import *
from tkinter import messagebox

import random


def func1():
    compliments=["best","buteful","greatest"]
    messagebox.showinfo("compliments",random.choice(compliments))
    

def func2():
    wishes=["good luck", "strong health", "fanny moments", "good day"]
    messagebox.showinfo("Wishes",random.choice(wishes))
    
def func3():
    wish=[" luck", "health", "fanny ", " day"]
    messagebox.showinfo("Wish",random.choice(wish))
tk=Tk()
btn1=Button(tk, text="get compliment", width=25, bg="#38F527", fg="black", command=func1)
btn1.pack()
btn2=Button(tk, text="get wishes", width=25, bg="#FA5B10", fg="black", command=func2)
btn2.pack()
btn3=Button(tk, text="get wish", width=25, bg="#FF15F8", fg="black", command=func3)
btn3.pack()

