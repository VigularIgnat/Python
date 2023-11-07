
from tkinter import *
from tkinter import filedialog as fd
FILE='front.jpg'
window=Tk()
window.title("Python Image viewer")
window.geometry('800x600')
label1=Label(window,text="Daйл:"+FILE)
label1.grid(column=1,row=1)
def showImage(F):
    viewer=Toplevel(window)
    viewer.title(F)
    img=PhotoImage(file=F)
    panel=Label(viewer,image=img)
    panel.image=img
    panel.grid(column=0,row=0)
def openFile():
   filetypes=(('Jpeg','*.jpg'),('PNG','*.png'))
   filename=fd.askopenfilename(title='Вiдкpити ³0браження',initialdir='.',filetypes=filetypes)
   FILE=filename
   label1.config(text="Daйn:"+FILE)
   showImage(filename)
btn=Button(window,text="Biдkрити þайл", соmmand=openFile())
btn.grid(column=1,row=0)
window.mainloop()

