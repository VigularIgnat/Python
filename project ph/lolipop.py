from tkinter import *
import random
number=0
root = Tk()
def func1():
 number=random.randint(1,10)
 tex.delete(1.0 , END)
 tex.insert(END, number)
ent =  Button(root,  text="random num", bg="purple",command=func1)
tex =  Text(root, width=9, bg="green", height=1, font="12",wrap=WORD)
tex.grid(row=0 ,column=2, padx=12,pady=10)
ent.grid(row=0 ,column=1, padx=12,pady=10)
root.mainloop()
