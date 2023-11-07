from tkinter import *
tk=Tk()

money_var=StringVar()
grn_sum=0

month_var=StringVar()
def func_grn():
    global grn_sum
    grn=money_var.get()
    month=month_var.get()
    month=int(month)
    grn=int(grn)
    
    for i in range(month):
        grn_pass=(grn*0.1)+grn
        grn_sum=grn_sum+grn_pass
    lbl2["text"]=str(grn_sum)
    

lbl=Label(tk, text="Введіть суму депозиту")
lbl.pack()

ent=Entry(tk, textvariable=money_var)
ent.pack()

lbl3=Label(tk, text="Введіть кількість місяців")
lbl3.pack()

ent2=Entry(tk, textvariable=month_var)
ent2.pack()

btn=Button(tk, text="Розрахувати", command=func_grn)
btn.pack()

lbl2=Label(tk, text=str(grn_sum))
lbl2.pack()
