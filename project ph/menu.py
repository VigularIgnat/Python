from tkinter import *
root=Tk()
def func1():
    win= Toplevel(root)
def func2():
    root.destroy()
def func3():
    lab=Label(root, text="add new")
    lab.pack()
m=Menu(root)
root.config(menu=m)
mm1=Menu(m)
m.add_cascade(label="File", menu=mm1)
mm1.add_command(label="Open, Ctrl+O")
mm1.add_command(label="close, Alt+F4")
mm1.add_command(label="Exit, Ctrl+Q ")

mm2=Menu(m)
m.add_cascade(label="Help", menu=mm2)
mm2.add_command(label="Idle help")
mm2.add_command(label="About")

mm3=Menu(m)
m.add_cascade(label="Options", menu=mm2)
mm3.add_command(label="configure")



mm1.add_command(label="New file, ctrl+N", command=func1)
mm1.add_command(label="Exit", command=func2)
mm2.add_command(label="About", command=func3)
root.mainloop()
