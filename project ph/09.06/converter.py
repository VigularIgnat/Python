from tkinter import *
n=0
grn=0
dol=0
def func1():
    global n
    grn=ent.get()
    kurs=ent2.get()
    kurs=int(kurs)
    grn=int(grn)
    n=grn/kurs
    n=round(n,2)
    lbl2['text']=str(n)
    
def func2():
    global n
    dol=ent.get()
    kurs=ent2.get()
    kurs=int(kurs)
    dol=int(dol)
    n=dol*kurs
    n=round(n,2)
    lbl2['text']=str(n)
root=Tk()

summ_var1=StringVar()
kurs_var1=StringVar()

lbl1=Label(root, text="Enter sum of money(grn)")
lbl1.pack()

ent=Entry(root, width=25,  textvariable=summ_var1)
ent.pack()
lbl3=Label(root, text="Enter kurs of money")
lbl3.pack()

ent2=Entry(root, width=25,  textvariable=kurs_var1)
ent2.pack()
btn=Button(root, width=25, text="Connvert dolar-grn", command=func1)
btn.pack()

btn2=Button(root, width=25, text="Connvert grn-dollar", command=func2)
btn2.pack()



lbl2=Label(root, text=str(n))
lbl2.pack()


