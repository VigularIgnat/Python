from tkinter import *
tk=Tk()

tk.title("Clicer")
n=0

def clicker(event):
    global n
    n=n+1
    label["text"]=str(n)
    



btn=Button(tk, width=40, height=12, text="click me", bg="green")
btn.pack()

btn.bind_all("<Button-1>", clicker)
label=Label(tk, text=str(n), font=("Helvetica"))
label.pack()
