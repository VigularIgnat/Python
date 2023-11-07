from tkinter import *
tk=Tk()
tk.title("shop")
su=90

def cand():
    su=+90
    text.insert(END,"90")
    
def ban():
    su=+25
    text.insert(END,"25")
def maslo():
    su=+35
    text.insert(END,"35")
def aplle():
    su=+12
    text.insert(END,"12")
def delet():
    su=0
    text.delete(1.0, END)
def ravn():
    text.insert(END,"=%s"%su)
        
candy=Button(tk, text="Цукерки", command=cand)
candy.grid(column=0,row=0, pady=10,padx=10)

apple=Button(tk,  text="Яблука", command=aplle)
apple.grid(column=1,row=0, pady=10,padx=10)

bana=Button(tk,  text="Банани", command=ban)
bana.grid(column=3,row=0, pady=10,padx=10)

muslo=Button(tk, text="масло", command=maslo)
bana.grid(column=0,row=1, pady=10,padx=10)

udal=Button(tk,text="<-", command=delet)
udal.grid(column=2,row=1, pady=10,padx=10)

ravno=udal=Button(tk,text="=", command=ravn)
udal.grid(column=3,row=1, pady=10,padx=10)

text=Text(tk,  width =10, bg="lightblue", height= 2, font="12", wrap=WORD)
text.grid(row=0, column= 2, padx=20, pady=10)
tk.mainloop()
