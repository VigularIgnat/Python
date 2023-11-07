from tkinter import*
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.title("Registration")
root.minsize(width=500, height=400)

name_var1=StringVar()
bool_var1=StringVar()
bool_var2=StringVar()
bool_var3=StringVar()
choice_var=StringVar()
choice_var1=StringVar()
choice_var1=b
def button_click():
    s=""
    s+=name_var1.get()+",Ви обрали:"
    if bool_var1.get():
        s+="distance 10 km"
    elif bool_var2.get():
        s+="distance 21 km"
    elif bool_var3.get():
        s+="distance 45 km"
    s+=choice_var1.get()+",Ви по гороскопу:
      if b=="autumn":
          s+="Ви рак"
    
    s+="у віковій категорії"+choice_var.get()

    
    
    
    messagebox.showinfo("Реєстрація", s)
    
lbl=Label(root, text="Input name, surname")
lbl.pack()

ent=Entry(root, width=30, textvariable=name_var1)
ent.pack()

prap1=Checkbutton(root, text="distanse 10 km", variable=bool_var1, onvalue="on", offvalue="off")
prap1.deselect()
prap1.pack()

prap2=Checkbutton(root, text="distanse 21 km", variable=bool_var2, onvalue="on", offvalue="off")
prap2.deselect()
prap2.pack()

prap3=Checkbutton(root, text="distanse 45 km", variable=bool_var3, onvalue="on", offvalue="off")
prap3.deselect()
prap3.pack()


choice=ttk.Combobox(root, width=25, textvariable=choice_var)
choice["values"]=("18-29", "30-39", "40-55")
choice.pack()


choice1=ttk.Combobox(root, width=25, textvariable=choice_var1)
choice1["values"]=("winter", "summer", "autumn", "spring")
choice1.pack()

btn=Button(root, text="Зареєструватися", command=button_click)
btn.pack()
