from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root=Tk()
root.minsize(width=300, height=300)
g=StringVar()

h=0
def func1():
    n=""
    global h
    en=ent.get()
    count=choice.get()
    count=int(count)
    food=food.get()
    food=str(food)
    
    if var1==1:
        g="На місці"
        h=h+0
    elif var1==2:
        g="З собою"
        h=h+30
        
    if food=="pizza":
        h=h+80
    elif food=="sushi":
        h=h+100
    elif food=="burger":
        h=h+60

    n="Your number of table "+ent.get()+"You food "+combo.get()+" "+food.get()+" "+g+" "+h
    
    lb4=Label(root, text=n)
    lb4.grid(row=8, column=2)




com_var1=StringVar()
choice_var=StringVar()
var1=IntVar()
var1.set(1)

lbl=Label(root, text="Виберіть замовлення")
lbl.grid(row=1, column=2)



lbl2=Label(root, text="Виберіть Столик")
lbl2.grid(row=2, column=1)

ent=Entry(root, width=10)
ent.grid(row=2, column=2)

list1=["pizza","shushi","burger"]
list2=["1","2","3","4","5"]


lbl3=Label(root, text="Виберіть їжу")
lbl3.grid(row=3, column=1)

food=ttk.Combobox(root, values=list1, width=25, variable=food)
food.grid(row=3, column=2)

lbl5=Label(root, text="Виберіть кількість")
lbl5.grid(row=4, column=1)

choice=ttk.Combobox(root, values=list2, width=25)
choice.grid(row=4, column=2)
             
rd=Radiobutton(root,text="На місці",  variable=var1, value=1)
rd.grid(row=5, column=2)


rd2=Radiobutton(root,text="З собою", variable=var1, value=2)
rd2.grid(row=6, column=2)             


btn=Button(root, text="Розрахувати",command=func1)
btn.grid(row=7, column=2)  


