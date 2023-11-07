import time
from tkinter import*

tk=Tk()
canvas=Canvas(tk, width=400, height=400)
canvas.pack()
rond=canvas.create_rectangle(10,10,25,25, fil='red')
canvas.itemconfig(rond, fill='blue')
canvas.itemconfig(rond, outline='black')

def move_rectangle(event):
    if event.keysym=='Up':
        canvas.move(1,0,-3)
    elif event.keysym=='Down':
        canvas.move(1,0,3)
    elif event.keysym=='Right':
        canvas.move(1,3,0)
    elif event.keysym=='Left':
        canvas.move(1,-3,0)
    else:
        canvas.move(1,3,3)
        
canvas.bind_all('<KeyPress-Up>', move_rectangle)
canvas.bind_all('<KeyPress-Down>', move_rectangle)
canvas.bind_all('<KeyPress-Right>', move_rectangle)
canvas.bind_all('<KeyPress-Left>', move_rectangle)
