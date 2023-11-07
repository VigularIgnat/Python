from tkinter import *
from tkinter import ttk
from tkinter import messagebox

tk=Tk()
ent=Entry(tk, width=10)
ent.grid(row=1, column=1)

def func1():
    run=""
    say=""
    com=g.get()
    if com=="woman":
        say="зарееструвалася"
    if com=="man":
        say="зарееструвався"
        
    run="Your"+" "+say+" "+"on course"
    lbl4=Label(tk,text=run)
    lbl4.grid(row=7, column=1)
    

list1=["Ui","Ux","coding"]
lbl=Label(tk,text="Name")
lbl.grid(row=1, column=2)

combo=ttk.Combobox(tk, values=list1, width=25)
combo.grid(row=2, column=1)

lbl2=Label(tk,text="Choice way of course")
lbl2.grid(row=2, column=2)

g=StringVar()

text_var=StringVar()

r1=Radiobutton(tk, variable=g, value="woman", text="woman" )
r1.grid(row=3, column=1)

r2=Radiobutton(tk, variable=g, value="man", text="man" )
r2.grid(row=4, column=1)

txt=Entry(tk, width=30, textvariable=text_var)
txt.grid(row=5, column=1)
   

lbl3=Label(tk,text="Write email")
lbl3.grid(row=5, column=2)

btn=Button(tk, text="count", command=func1)
btn.grid(row=6,column=1)

