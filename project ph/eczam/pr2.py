from tkinter import *
tk=Tk()
lbl=Label(tk, text="Регистрация пользователя", font=14)
lbl.grid(row=0, column=1)
tk.minsize(width="800", height="650")

def func_check():
    x=""
    n=ent3.get()
    x="Вас"+" "+ent.get()+" "+"зареєстровано"

    if n=="123":
        ltl=Label(tk,text=x,)
        ltl.grid(row=14, column=1)
    else:
        ltl2=Label(tk,text="введите пароль еще раз",fg="red")
        ltl2.grid(row=8, column=3)

def func_dest():
    tk.destroy()






lbl=Label(tk,text="", font=9)
lbl.grid(row=3, column=1)


lbl3=Label(tk,text="*Обязательное поле", font=9)
lbl3.grid(row=4, column=1)


lba=Label(tk,text="", font=9)
lba.grid(row=5, column=1)


lbl4=Label(tk,text="Имя*", font=9)
lbl4.grid(row=6, column=1)

ent=Entry(tk, width=40)
ent.grid(row=6, column=2)

lbl5=Label(tk,text="Логин*", font=9)
lbl5.grid(row=7, column=1)

ent2=Entry(tk, width=40)
ent2.grid(row=7, column=2)

lbl6=Label(tk,text="Пароль*", font=9)
lbl6.grid(row=8, column=1)


ent3=Entry(tk, width=40)
ent3.grid(row=8, column=2)

lbl6=Label(tk,text="Повтор пароля*", font=9)
lbl6.grid(row=9, column=1)

ent4=Entry(tk, width=40)
ent4.grid(row=9, column=2)

lbl7=Label(tk,text="Адрес електронной почты*", font=9)
lbl7.grid(row=10, column=1)

ent5=Entry(tk, width=40)
ent5.grid(row=10, column=2)

lbl8=Label(tk,text="Потверждение адреса електронной почты", font=9)
lbl8.grid(row=11, column=1)

ent6=Entry(tk, width=40)
ent6.grid(row=11, column=2)

lnn=Label(tk,text="")
lnn.grid(row=12, column=1)

btn=Button(tk, text="Реєстрация", fg="white", bg="blue", command=func_check)
btn.grid(row=13, column=1)

btn=Button(tk, text="Отмена", fg="Black", command=func_dest)
btn.grid(row=13, column=2)
