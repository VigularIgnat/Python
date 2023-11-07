from tkinter import*
from tkinter.filedialog import*
import fileinput

def func1():
    opn=askopenfilename()
    for i in fileinput.input(opn):
        text.insert(END,1)

def func2():
    sav=asksaveasfilename()
    lat=text.get(1,0, END)
    nk= open(sav,"w")
    nk.write(lat)
    nk.close()

root=Tk()

m=Menu(root)
root.config(menu=m)

mm1=Menu(m)
m.add_cascade(label="File", menu=mm1)

mm1.add_command(label="open...", command=func1)

mm1.add_command(label="Save...", command=func2)

tex=Text(root, width=50, height=20, font="12")
tex.pack()

root.mainloop()
