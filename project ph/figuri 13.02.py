from tkinter import *
tk=Tk()
def oval_func(event):
    c.delete(oval)
    c.create_text(80,50,text="круг")

def rect_func(event):
    c.delete(rect)
    c.create_text(280,50,text="прямокутник")

def triangle(event):
    c.delete(trian)
    c.create_text(380, 50,
                  text="Треугольник")
def kolo_func(event):
    c.delete(kolo)
    c.create_text(480, 50, text="Коло")
    
c= Canvas(width=660, height=400, bg="grey80")
c.pack()

oval=c.create_oval(30,10,130,80, fill='orange')

rect=c.create_rectangle(180, 10, 280, 80,
                   fill="lightgreen")
trian= c.create_polygon(330,80,380,10,430, 80,
                         fill="white", outline="black")
kolo=c.create_oval(30,299,90,80, fill= "red")
c.tag_bind(oval, '<Button-1>', oval_func)
c.tag_bind(rect, '<Button-1>', rect_func)
c.tag_bind(trian, '<Button-1>', triangle)
c.tag_bind(kolo, '<Button-1>', kolo_func)
tk.mainloop()
