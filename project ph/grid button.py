from tkinter import *
root=Tk()
root.title(" methon grid")

btn=Button(root, width=25, height=10, bg="grey", fg="black",  text="button1")
btn2=Button(root, width=25, height=10, bg="yellow", fg="black",  text="button1")
btn.grid(row=0, column=0, padx=5, pady=10)
btn2.grid(row=1, column=1, padx=5, pady=10)
btn3=Button(root, width=25, height=10, bg="grey", fg="black",  text="button1")
btn3.grid(row=2, column=2, padx=5, pady=10)

root.mainloop()
 
