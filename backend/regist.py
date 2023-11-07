

from tkinter import *


register={}

class Cite:
    
    def __init__(self):
        
        self.password_ent=StringVar()
    def function_add(self):
        self.password=input("Write your name")
        self.email=input("Enter your email")
        if self.email in register:
            print("This name was used")
        else:
            register[self.email]=self.password
            function_registration()

    def function_registration(self):
        self.email_ent=StringVar()
        root=Tk()
        root.minsize(width=200, height=200)
        lbl=Label(root,text="Sing in or sign up")
        lbl.pack()
        ent=Entry(root,textvariable=selfemail_ent)
        ent.pack()


    


cite_create=Cite()
    


