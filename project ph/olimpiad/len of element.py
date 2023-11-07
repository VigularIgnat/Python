from tkinter import *

tk=Tk()


var1=StringVar()
k=0
def func1(event):
    global k
    s=var1.get()
    k=0
    
    for i in s:
        k+=1
    lbl["text"]=str(k)

lbl1=Label(tk, text="count quantity")
lbl1.pack()

ent=Entry(tk, textvariable=var1)
ent.pack()

lbl=Label(tk, text=str(k))
lbl.pack()

ent.bind("<Return>", func1)
