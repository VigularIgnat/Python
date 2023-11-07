from tkinter import*
import time
tk=Tk()
canvas=Canvas(tk, width=500, height=400, bg="green")
canvas.pack()
pram=canvas.create_rectangle(10,150,20,350, fill="blue")
pram2=canvas.create_rectangle(490,150,480,350, fill="blue")
kolo=canvas.create_oval(230,210,270,250, fill="yellow")
def turn_left(event):
    pram.move(0,1,-10)
def turn_right(self,event):
    pram.move(0,1,10)
def turn_left1(self,event):
    pram2.move(0,2,-10)
def turn_right1(self,event):
    pram2.move(0,2,10)
canvas.bind_all("<KeyPress-Left>",turn_left )
canvas.bind_all("<KeyPress-Right>", turn_right)
canvas.bind_all("<KeyPress-Left>", turn_left1)
canvas.bind_all("<KeyPress-Right>", turn_right1)

