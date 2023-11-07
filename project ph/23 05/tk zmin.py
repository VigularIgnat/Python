from tkinter import *
n=0

def click_button():
    global n
    n=n+1
    root.title("Clicks []",format(n))

root=Tk()
root.title("GUI на Pyton")
root.geometry("300x250")

btn=Button(root,text="click me", bg="#555", fg="#ccc", padx="20", pady="6", font="16", command=click_button)
btn.pack()

root.mainloop()
