from tkinter import *
root=Tk()
root.title("Main Window")
but= Button(root, text="Виконати", width=50, height=50, bg="black", fg="yellow", command=func2)
but.pack()
def func1():
    root.destroy()
def func2():
    print("Привіт, введи свій вік")
def func3():
    s=ent.get()
    d= s+10
ent=Entry(root, text="Введи вік", dg="blue", fg="yellow")
m=Menu(root)
root.config(menu=m)
mm1=Menu(m)
tex= Text(
m.add_cascade(label="File", menu=mm1)
mm1.add_command(label="Close, ctrl+N", command=func1)
ent.pack()
root.mainloop()

