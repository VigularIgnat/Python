from tkinter import*
tk=Tk()
def del_oval(event):
    c.delete(oval)
    c.create_text(80, 50, text="круг")
def del_trian(event):
    c.delete(rect)
    c.create_text(230,50, text="прямокутник")
def del_rect(event):
    c.delete(trian)
    c.create_text(380,50, text="трикутник")
def del_tr(event):
    c.delete(tr)
    c.create_text(400,50, text="щось")

    
c= Canvas(tk, width=560, height=100, bg="grey80")
c.pack()

oval=c.create_oval(30, 10, 130,80, fill="red", outline="black")
rect=c.create_rectangle(180,10,280,80, fill="blue")
trian=c.create_polygon(330,80,380,10,430,80, fill="yellow")
tr=c.create_polygon(400,10,420,30, 460,10,460,20, fill="green")
c.tag_bind(oval,'<Button-1>',del_oval)
c.tag_bind(rect,'<Button-1>',del_trian)
c.tag_bind(trian,'<Button-1>',del_rect)
c.tag_bind(tr,'<Button-1>',del_tr)
tk.mainloop()
