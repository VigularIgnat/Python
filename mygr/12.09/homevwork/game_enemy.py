import random
from tkinter import *
from tkinter import ttk
import time

tk=Tk()
tk.minsize(width=600,height=400)
root=Tk()
root.minsize(width=100,height=100)

enemy={}
main_character={}


name_person=StringVar()
name_person_finally=name_person.get()

list_level=["Hard","Easy", "Medium"]
list_color=["Black","Green", "Yellow","Red"]

lbl_choose=Label(root, text="Choose color of your enamy")
lbl_choose.grid(row=2, column=0)

combo_color=ttk.Combobox(root, values=list_color)
combo_color.grid(row=2, column=1)

lbl_level=Label(root, text="Choose level")
lbl_level.grid(row=4, column=0)


combo_level=ttk.Combobox(root, values=list_level)
combo_level.grid(row=4, column=1)

lbl_name=Label(root,text="Write your name")
lbl_name.grid(row=5, column=0)

name_entry=Entry(root, width=10, textvariable=name_person)
name_entry.grid(row=5,column=1)

lbl_color=Label(root,text="Select color for your")
lbl_color.grid(row=6,column=0)

combo_color_person=ttk.Combobox(root, values=list_color)
combo_color_person.grid(row=6, column=1)

canvas = Canvas(tk, width=600, height=400, bg='white')
canvas.pack()

#function enemy
def enemy_create():
    
    combo_color_person_finally=combo_color_person.get()
    combo_level_finally=combo_level.get()
    combo_color_finally=combo_color.get()
    person=canvas.create_rectangle(285,340,315,370, fill=combo_color_person_finally)
    canvas.move(person,200,300)
    x=0
    canvas.bind_all('<KeyPress-Left>', turn_left)
    canvas.bind_all('<KeyPress-Right>',turn_right)
    if combo_level_finally=="Hard":
        for i in range(100):
            x_position=random.randint(-570,570)
            y_position=10
            width_hard_level=30
            enemy=canvas.create_rectangle(x_position, y_position, x_position+width_hard_level, y_position+width_hard_level,fill=combo_color_finally)
            tk.update()
            time.sleep(0.2)
        
    if combo_level_finally=="Easy":
        for i in range(100):
            x_position=random.randint(-570,570)
            y_position=10
            width_hard_level=30
            enemy=canvas.create_rectangle(x_position, y_position, x_position+width_hard_level, y_position+width_hard_level,fill=combo_color_finally)
            tk.update()
            time.sleep(0.5)
    if combo_level_finally=="Medium":
        for i in range(100):
            x_position=random.randint(-570,570)
            y_position=10
            width_hard_level=30
            enemy=canvas.create_rectangle(x_position, y_position, x_position+width_hard_level, y_position+width_hard_level,fill=combo_color_finally)
            tk.update()
            time.sleep(0.3)
pos=canvas.coords(person)                
def turn_rigth(event):
    canvas.move(person,x,0)
    x=x+5
def turn_left(event):
    canvas.move(person,x,0)
    x=x+5
    
    
btn_start=Button(root, text="Start", command=enemy_create)
btn_start.grid(row=7, column=2)




    
