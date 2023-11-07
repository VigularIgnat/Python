from tkinter import *
import random
import time

class Ball:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_oval(10,10,25,25, fill=color)
        self.canvas.move(self.id, 245,100)
        self.id1=canvas.create_oval(10,10,25,25, fill=color)
        self.canvas.move(self.id1, 245,100)
        starts=[-3,-2,-1,2,2,3]
        random.shuffle(starts)
        self.x=starts[0]

        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        
    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=3
        if pos[3]>=self.canvas_height:
            self.y=-3
            
    def draw1(self):
        self.canvas.move(self.id1,self.x,0)
        pos=self.canvas.coords(self.id1)
        
        if pos[0]<=0:
            self.x=5
        if pos[2]>=self.canvas_width:
            self.x=-5
        
tk=Tk()
tk.title("game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk, width=500, height=400, bd=0,highlightthickness=0)
canvas.pack()
tk.update()

ball=Ball(canvas, "green")
ball1=Ball(canvas, "blue")
while 1:
    ball.draw()
    ball1.draw1()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)    


