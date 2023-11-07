from tkinter import*
from tkinter import ttk
from tkinter import messagebox
tk= Tk()
tk.title("registration")
boo1=StringVar()
boo2=StringVar()
boo3=StringVar()
choice=StingVar()
name_var1=StringVar()
def button_click():
    s=""
    s+=name_var1.get()+",Ви обрали:"
    if bool_var1.get():
        s+="distance 10 km"
    elif boo2.get():
        s+="distance 21 km"
    elif boo3.get():
        s+="distance 45 km"
    s+="у віковій категорії"+choice.get()
    
    messagebox.showinfo("Реєстрація", s)


lbl=Label(tk, fg="red", text="Write name surname")
lbl.pack()

ck1=Checkbutton(tk,text="distanse 10 km", variable=boo1, onvalue="on", offvalue="off")
ck1.deselect()
ck1.pack()

ck2=Checkbutton(tk,text="distanse 20 km", onvalue="on", offvalue="off", varaible=boo2)
ck2.deselect()
ck2.pack()

ck3=Checkbutton(tk,text="distanse 30 km", variable=boo3, offvalue="off", onvalue="on")
ck3.deselect()
ck3.pack()

choice=ttk.Combobox(root, width=25, textvariable=choice)
choice["values"]=("18-29", "30-39", "40-55")
choice.pack()

ent=Entry(root, width=30, textvariable=name_var1)
ent.pack()


