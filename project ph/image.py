from tkinter import *
tk=Tk()
tk.title("Днем народження")
canvas=Canvas(tk, width=1000, height=1000)
canvas.pack()

my_image=PhotoImage(file='')
canvas.create_image(0,0, anchor=NW, image=my_image)
tk.mainloop()
