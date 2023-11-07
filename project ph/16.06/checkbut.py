from tkinter import*
tk=Tk()

var1=StringVar()
var2=StringVar()


lis=Listbox(tk, bg="yellow", height=3)
lis.grid(row=4, column=1)

prap1=Checkbutton(tk,text="First", variable=var1, onvalue="first input", offvalue="fist output")
prap1.grid(row=1, column=1)
prap1.deselect()

prap2=Checkbutton(tk, text="Second", variable=var2, onvalue="second input", offvalue="second output")
prap2.grid(row=2, column=1)
prap2.deselect()

def func1():
    v1=var1.get()
    v2=var2.get()
    l=[v1, v2]
    lis.delete(0,1)
    for i in l:
        lis.insert(END, i)
btn=Button(tk, text="Value of checkbox", command=func1)
btn.grid(row=3, column=1)

tk.mainloop()
