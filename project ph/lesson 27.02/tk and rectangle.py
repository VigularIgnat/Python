from tkinter import *
import time

def func1(event):
    if event.keysym=="Left":
        canvas.move(1,-5,0)
    if event.keysym=="Right":
        canvas.move(1,5,0)
        
tk=Tk()        
canvas=Canvas(tk, width=500, heigh=400, bg="black")
canvas.pack()
canvas.create_rectangle(200,380,300,400, fill="yellow")
canvas.create_oval(225,10,250,60, fill="white")
canvas.create_oval(10,185,40,215, fill="green")
for i in range(0,60):
    canvas.move(2,0,5)
    canvas.move(3,8,0)
    tk.update()
    time.sleep(0.01)
    
canvas.bind_all('<KeyPress-Left>', func1)
canvas.bind_all('<KeyPress-Right>', func1)




