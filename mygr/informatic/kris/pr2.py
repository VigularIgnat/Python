from tkinter import *


prices={
    0:15,
    1:30,
    2:50
    }
tk=Tk()

tk.minsize(400,400)
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
elem_price=0


for i in range(3):
    elem_price+= prices[i]
    

def count():
    var1_res=var1.get()
    var2_res=var2.get()
    var3_res=var3.get()
    var4_res=var4.get()
    list1=[]
    
    if var1_res==10 and var2_res==10 and var3_res==10:
        list1=[]
        lb2["text"]="Нічого не вибрано"
    money=int(ent.get())
    if var1_res!=10 and var2_res!=10 and var3_res!=10 and var4_res!=10:
        
        res=0
        list1=[var1_res, var2_res, var3_res]
        for i in list1:
            res=res+prices[i]
        res+=prices[0]
        if money >= res:
            lb2["text"]="Вистачить, залишок "+ str(money-res)
        else:
            lb2["text"]="Не вистачить "+ str(res- money)
    elif var2_res!=10 and var3_res!=10:
        res=0
        list1=[var2_res, var3_res]
        for i in list1:
            res=res+prices[i]
        if money >= res:
            lb2["text"]="Вистачить, залишок "+ str(money-res)
        else:
            lb2["text"]="Не вистачить"+ str(res- money)

    elif  var1_res!=10 and var2_res!=10:
        res=0
        list1=[var1_res, var2_res]
        for i in list1:
            res=res+prices[i]
        if money >= res:
            lb2["text"]="Вистачить, залишок "+ str(money-res)
        else:
            lb2["text"]="Не вистачить"+ str(res- money)
    elif var1_res!=10 and var3_res!=10:
        res=0
        list1=[var1_res, var3_res]
        for i in list1:
            res=res+prices[i]
        if money >= res:
            lb2["text"]="Вистачить, залишок "+ str(money-res)
        else:
            lb2["text"]="Не вистачить"+ str(res- money)
    else:
        if var1_res!=10:
            res=res+prices[0]
            if money >= res:
                lb2["text"]="Вистачить, залишок "+ str(money-res)
            else:
                lb2["text"]="Не вистачить"+ str(res- money)
        elif var2_res!=10:
            res=res+prices[1]
            if money >= res:
                lb2["text"]="Вистачить, залишок "+ str(money-res)
            else:
                lb2["text"]="Не вистачить"+ str(res- money)
        elif var3_res!=10:
            res=res+prices[2]
            if money >= res:
                lb2["text"]="Вистачить, залишок "+ str(money-res)
            else:
                lb2["text"]="Не вистачить"+ str(res- money) 
    


   
        
lbl=Label(tk, text="Shop")
lbl.pack()

ent=Entry(tk,width=10)
ent.pack()

btn=Button(tk, text="Розрахувати", command=count)
btn.pack()

lb2=Label(tk)
lb2.pack()

c1 = Checkbutton(tk, text='Хліб',variable=var1, onvalue=0, offvalue=10) 
c1.pack()
c2 = Checkbutton(tk, text="Молоко",variable=var2, onvalue=1, offvalue=10)
c2.pack()

c3 = Checkbutton(tk, text="Печиво 400г",variable=var3, onvalue=2, offvalue=10)
c3.pack()

lb3=Label(tk, text="Додатково")
lb3.pack()


c3 = Checkbutton(tk, text="+1 Хліб",variable=var4, onvalue=2, offvalue=10)
c3.pack()

