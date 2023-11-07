from tkinter import *
root=Tk()
root.title("Main Window")

top1=Toplevel(root, bd=120, bg="yellow")
top1.title("Window in chekbox")
top1.minsize(width=200, height=60)

top2= Toplevel(root, bd=120, bg="light blue")
top2.title("window of Radiobutton")
top2.minsize(width=200, height=60)

a1=StringVar()
a2=StringVar()

prap1=Checkbutton(top1,text="Type", variable=a1)
prap2=Checkbutton(top1, text="Name", variable=a2)

a3=IntVar()

rad1=Radiobutton(top2, text="Without filling", variable=a3, value=1)
rad2=Radiobutton(top2, text="Gradient fill", variable=a3, value=2)
but=Button(root, text="Start", width=30, height=5, bg="white", fg="red")
prap1.deselect()
prap2.deselect()
but.pack()
prap1.pack()
prap2.pack()
rad1.pack()
rad2.pack()
root.mainloop()
