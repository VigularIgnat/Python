from tkinter import *
root=Tk()
def funcil():
    s=ent.get()
    if s== "Lamborgini":
        tex.delete(1.0, END)
        tex.insert(END, "This concert made in Italy")
        
    elif s == "Sitroen":
        tex.delete(1.0, END)
        tex.insert(END, "This consert made in France")
    elif s == "Aston Martin":
        tex.delete(1.0, END)
        tex.insert(END, "This consert made in Great Britan")
    elif s == "Renault":
        tex.delete(1.0, END)
        tex.insert(END, "This consert made in France")
    elif s == "Mersedes":
        tex.delete(1.0, END)
        tex.insert(END, "This consert made in German")
    elif s == "BMW":
        tex.delete(1.0, END)
        tex.insert(END, "This consert made in German")
    elif s == "Opel":
        tex.delete(1.0, END)
        tex.insert(END, "This consert made in German")
    elif s == "Pegoeut":
        tex.delete(1.0, END)
        tex.insert(END, "This consert made in France")
    else:
        tex.delete(1.0, END)
        tex.insert(END, "Sorry we haven't this consert in book")
ent=Entry(root, width= 10, bg="red")
but=Button(root, text="Play", bg="magenta", command= funcil)
tex=Text(root, width =20, bg="lightblue", height= 4, font="12", wrap=WORD)
ent.grid(row=0, column= 0, padx=2, pady=10)
but.grid(row=0, column= 1, padx=12, pady=10)
tex.grid(row=0, column= 2, padx=20, pady=10)
root.mainloop()
