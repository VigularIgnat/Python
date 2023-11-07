from tkinter import *

tk=Tk()
tk.minsize(400, 500)
tk.title("First page")
label= Label(tk, text="Quiz")
label.pack()


def hello():
    root=Tk()
    root.minsize(440,600)

button= Button(tk, text="Click please",command=hello(), width=10, height=1, bg="blue", fg="yellow", font="Arial 14")

button.pack()
