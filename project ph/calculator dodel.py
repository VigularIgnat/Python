from tkinter import*
import math
root=Tk()
root.title("Calculator")
root.config(bg="Black")
operations=["/", "*","+","-", "-", "C"]
text=''

def addtowork(obj):
    global text
    text= str(text)
    if obj == "=":
        try:
            textfield.config(text=eval(text))
            text=eval(text)
        except Exception as ex:
            gotit= textfield.cget("text")
            textfield.config(text="Invalid syntaxys")
            text= ''
    elif obj=="C":
        if len(text) == 0:
            pass
        else:
            text = text[:-1]
            textfield.config(text=text)
    else:
        text += str(obj)
        textfield.config(text=text)
framebtn=Frame(root, bg="black")
framebtn.grid(row=1, column=0)
test={9: 0, 8: 1, 7:2, 6:3, 5:4, 4:5, 3:6, 2: 7, 1:8, 0: 9}
test2={10: "/", 1: "*", 2: "+", 3:"-", 4:"-", 5: "C"}
size= 4
for k,v in test.items():
    i=k
    num=v
    if num != 0:
        Button(framebtn, bg="black", fg="white", text= str(num),
               command=lambda n=num :
               addtowork(n), height=size, width=size).grid(row=i//3,
                                                        column=i%3, sticky="news")
    else:
        Button(framebtn, bg="black", fg="white", text=str(num),
                command=lambda n=num : aadtowork(n), height=size,
                width=size).grid(row=3, column=2, stiсky="nesw")
textfield= Label(root, bg="black", fg="white")
textfield.grid(row=0,column=0, columnspan=3)

for k,o in test2.items():
    if o== "C":
        Button(framebtn, bg="black", fg="white", text=0,
               command=lambda op=o: addtowork(op), height=size,
               width=size).grid(row=3, column=0, stiсky="nesw")
    elif o=="=":
        Button(framebtn, bg="black", fg="white", text=o,
               command=lambda op=o : addtowork(op), height=size,
               width=size).grid(row=3, column=2, sticky="nesw")
    else:
        Button(framebtn, bg="black", fg="white", text=o,
               command=lambda op=o : addtowork(op), height=size,
               width=size).grid(row=k, column=3, sticky="nesw")
        
mainloop()
