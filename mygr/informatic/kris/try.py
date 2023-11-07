from tkinter import *

bread=10
cookie=40
milk=30

tk=Tk()

tk.minsize(400,400)
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()

def count():
    var1_res=var1.get()
    var2_res=var2.get()
    var3_res=var3.get()
    var4_res=var4.get()
    money=int(ent.get())
    if var1_res==10 and var2_res==10 and var3_res==10 and var4_res==10:
        lb2["text"]="Нічого не вибрано"
    
        
    elif var1_res!=10 and var2_res!=10 and var3_res!=10 and var4_res!=10:
        res= bread+cookie+milk*2
        if money >= res:
            lb2["text"]="Вистачить, залишок "+ str(money-res)
        else:
            lb2["text"]="Не вистачить, потрібно ще "+ str(res- money)
    else:
        lb2["text"]="Ви вибрали не все що вам потрібно"

        
lbl=Label(tk, text="Shop")
lbl.pack()

ent=Entry(tk,width=10)
ent.pack()

btn=Button(tk, text="Розрахувати", command=count)
btn.pack()

lb2=Label(tk)
lb2.pack()

c1 = Checkbutton(tk, text='Хліб',variable=var1, onvalue=4, offvalue=10) 
c1.pack()
c2 = Checkbutton(tk, text="Молоко",variable=var2, onvalue=1, offvalue=10)
c2.pack()

c3 = Checkbutton(tk, text="Печиво",variable=var3, onvalue=2, offvalue=10)
c3.pack()

lb3=Label(tk, text="Додатково")
lb3.pack()


c4 = Checkbutton(tk, text="+1 Хліб",variable=var4, onvalue=3, offvalue=10)
c4.pack()

