import random
from tkinter import *
from tkinter import ttk

tk=Tk()
tk.minsize(width=200,height=200)
tk.title("Pizzeria")

int_combo=IntVar()

order={}
ingredients=[]

ingredients_ent=StringVar()

ingredients_finally=ingredients_ent.get()

menu_list=["pizza","sushi","borsh","soup"]
quentity_list=[1,2,3,4,5]

lbl_pizzeria=Label(tk, text="Our menu")
lbl_pizzeria.pack()

combo_menu=ttk.Combobox(tk, values=menu_list)
combo_menu.pack()

combo_quetity=ttk.Combobox(tk, values=quentity_list, textvariable=int_combo)
combo_quetity.pack()
int_combo.get()
for i in range(3):
    dish=combo_menu.get()
    ent_ing=Entry(tk,textvariable=ingredients_ent)
    ent_ing.pack()
    for elem in range(3):
        ingredients_finally

