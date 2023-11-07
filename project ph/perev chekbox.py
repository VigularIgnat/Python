from tkinter import *
root=Tk()
root.title("Main Window")
var1=StringVar()
var2=StringVar() 
prap1=Checkbutton(root,text="First", variable=var1, onvalue="first input", offvalue="Fisrst output")
prap2=Checkbutton(root, text="second",variable=var2, onvalue="second input", offvalue="Second output")
lis=Listbox(root, bg="yellow", height=3)
def func1():
    v1=var1.get()
    v2=var2.get()
    l=[v1,v2]
    lis.delete(0,1)
    for i in l:
        lis.insert(END, i)
but=Button(root, text="Value of checkBox", command=func1)
prap1.deselect()
prap2.deselect()
prap1.pack()
prap2.pack()
but.pack()
lis.pack()
root.mainloop()
