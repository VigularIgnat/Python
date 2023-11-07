from tkinter import*
from tkinter.ttk import*

root=Tk()
root.title("Resizible")
root.geometry('250x250')

Label(root, text"It/'s resible").pack(side=TOP, pady=10)
root.resiziable(0,0)
root.mainloop()
