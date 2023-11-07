from tkinter import *

tk=Tk()

w= 300000

def count():
    res=int(entry.get())
    final_num=w*res
    lbl_res["text"]=str(final_num)+" км"


tk.minsize(width="300", height="300")

lbl=Label(tk, text="Розрахувати швидкість з часом")

entry=Entry(tk, width="20")
entry.pack()

lbl_res=Label(tk)
lbl_res.pack()


btn=Button(tk, text="Розрахувати", command=count)
btn.pack()

