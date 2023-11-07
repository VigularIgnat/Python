from tkinter import *
root=Tk()
root.title("window")
root.minsize(width=200, height=60)
def func1():
    a=int(input("input number"))
    b=int(input("input number"))
    s=a+b
    print(s)
def func2():
    win=Toplevel(root)
def func3():
    root.destroy()
def func4():
    lab=Label(root, text="...info about Python")
    lab.pack()
def func5():
    lab=Label(root, text="Vigulyar Ignat")
    lab.pack()
a1=StringVar()
a2=StringVar
a3=IntVar()

btn=Button(root,text="Button", bg="yellow", fg="black", width=25,command=func1)
ent=Entry(root, bg="blue", width=10)

tex=Text(root, width =20, bg="lightblue", height= 4, font="12", wrap=WORD)

chd=Checkbutton(root, text="Name",variable=a1, onvalue="first input", offvalue="first output")
chd2=Checkbutton(root, text="Name",variable=a2, onvalue="second input", offvalue="second output")

rdb=Radiobutton(root, text="Gr fill",variable=a3)
rdb2=Radiobutton(root, text="fall",variable=a3)

m=Menu(root)
root.config(menu=m)
mm1=Menu(m)
m.add_cascade(label="File", menu=mm1)
mm1.add_command(label="Open, Ctrl+O", command=func2)
mm1.add_command(label="close, Alt+F4")
mm1.add_command(label="Exit, Ctrl+Q ",command=func3)

mm2=Menu(m)
m.add_cascade(label="Help", menu=mm1)
mm1.add_command(label="About python, Ctrl+O", command=func4)
m3=Menu(root)
root.config(menu=m3)
mm2=Menu(m)
m.add_cascade(label="Author", menu=m3)
mm1.add_command(label="About python, Ctrl+O", command=func5)

ent.grid(row=0, column=0, padx=2, pady=10)
btn.grid(row=1, column=1, padx=12, pady=10)
tex.grid(row=0, column=1, padx=12, pady=10)
chd.deselect()
chd.grid(row=3, column=3, padx=24, pady=10)
rdb.grid(row=3, column=3, padx=24, pady=10)
chd2.pack()
rdb2.pack()
root.mainloop()

