from tkinter import*
import random
def funcrundom():
    a=random.randint(10,100) 
    b=random.randint(10,100) 
    c=random.randint(10,100)
    print('''first nomber- %s 
    second nomber -%s
    third- %s'''% (a,b,c))
root=Tk
but1=Button(root)
but1=Button(root, text="yrour rd number", width=50, heigh=60 command=funcrundom)
root.mainloop
