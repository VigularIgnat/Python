from tkinter import  *
tk= Tk()
tk.minsize(width="400", height="400")

tk.title("Name, surname")

lbl=Label(tk, text="We on the site")
lbl.pack()

btn=Button(tk, text="Click me", fg="red")
btn.pack()

ent=Entry(tk, width=10)
ent.pack()



