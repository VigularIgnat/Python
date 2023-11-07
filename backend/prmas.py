from tkinter import *
import random
from tkinter import ttk

tk=Tk()
tk.minsize(width="300", height="300")
def create_window():
    window = Toplevel(root) 


root = Tk()
b = Button(root, text="Create new window", command=create_window)
b.pack()


#tk
quaes=StringVar()
mas18=[]
mas29=[]
mas45=[]
ms1=len(mas18)
ms2=len(mas29)
ms4=len(mas45)
def check():
    lb3=Label(tk,text=ms1)
    lb3.pack()
   



for i in range(10):
    yer=quaes.get()
    if yer=="18-28":
        mas18.append(yer)
    elif yer=="29-45":
        mas29.append(yer)
    elif yer=="45 and hight":
        mas45.append(yer)
    


list1=["18-28","29-45","45 and hight", "Nothing"]


lb2=Label(tk,text="Choose your year",)
lb2.pack()
combo=ttk.Combobox(tk, values=list1, width=25, textvariable=quaes)
combo.pack()
bt3=Button(tk,text="check", command=check)
bt3.pack()

#root
qv_many=StringVar()

qual=qv_many.get()


lb1=Label(root, text="How mny peopel delay")
lb1.pack()
ent1=Entry(root, textvariable=qv_many)
ent1.pack()



root.mainloop()
tk.mainloop()



