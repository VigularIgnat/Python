from tkinter import *
tk=Tk()
c=Canvas(tk, width=300, height=300, bg="white")
c.pack()

c.create_oval(100,100,200, 200, fill="red")

def func_zac():
    tk.destroy()
def func_clean():
    c.delete("all")

def fun_del_canva():
    tk.delete(c)
    
btn1=Button(tk, text="delete",command=func_clean)
btn1.pack()

btn2=Button(tk, text="exit", command=func_zac)
btn2.pack()



