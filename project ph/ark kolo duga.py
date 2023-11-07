from tkinter import *
from tkinter import colorchooser
import random
tk=Tk()
canvas=Canvas(tk, width=500, height=500)
canvas.pack()

def func1():
    canvas.create_arc(10,10, 200, 80, extent=45, style=ARC)
    canvas.create_arc(10,80, 200, 160, extent=90, style=ARC)
    canvas.create_arc(10,10, 200, 240, extent=135, style=ARC)
    canvas.create_arc(10,10, 200, 320, extent=180, style=ARC)
    canvas.create_arc(10,10, 200, 400, extent=359, style=ARC)
def func2():
    canvas.create_polygon(200,10,240,30, 120, 100, 140,120)

def func3():
    def random_rectangle(width, height):
        x1=random.randrange(width)
        y1=random.randrange(height)
        x2=x1+random.randrange(width)
        y2=y1+random.randrange(height)
        canvas.create_rectangle(x1,y1,x2,y2)
    for i in range(0,100):
        random_rectangle(200,200)
def random_rectangle(width, height, fill_color):
    x1=random.randrange(width)
    y1=random.randrange(height)
    x2=x1+random.randrange(width)
    y2=y1+random.randrange(height)
    canvas.create_rectangle(x1,y1,x2,y2, fill=fill_color)
colorchooser.askcolor()
c=colorchooser.askcolor()
random_rectangle(400,400,c[1])
random_rectangle(400, 400, 'green')



    

btn=Button(tk, text="draw arc",command=func1)
btn.pack()
btn2=Button(tk, text="draw polygon", command=func2)
btn2.pack()
btn3=Button(tk, text="draw rectangle", command=func3)
btn3.pack()
btn4=Button(tk, text="draw color rectangle ")
btn4.pack()
