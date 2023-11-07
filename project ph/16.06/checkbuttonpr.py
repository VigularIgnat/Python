from tkinter import*

tk=Tk()

var1=StringVar()


lbl=Label(tk, text="Input Name ang Surname")
lbl.grid(row=1, column=1)

def func1():
    n=""
    n=ent.get()+"ou favourite color is "+var1.get()
    lbl=Label(tk, text=n)
    lbl.grid(row=7, column=1)


ent=Entry(tk, width=25)
ent.grid(row=1, column=2)

lbl=Label(tk, text="Choise the colour")
lbl.grid(row=2, column=1)

check=Checkbutton(tk, text="red", onvalue="red", offvalue="off", variable=var1)
check.deselect()
check.grid(row=3, column=1)

check2=Checkbutton(tk, text="orange", onvalue="orange", offvalue="off", variable=var1)
check2.deselect()
check2.grid(row=4, column=1)

check3=Checkbutton(tk, text="green", onvalue="green", offvalue="off", variable=var1)
check3.deselect()
check3.grid(row=5, column=1)

btn=Button(tk, text="Input", command=func1)
btn.grid(row=6, column=1)
