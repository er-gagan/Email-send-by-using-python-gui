from tkinter import *

root=Tk()
root.geometry("750x458")
root.title("Send Email")

photo = PhotoImage(file="./ico.png")
root.iconphoto(False,photo)

image1 = PhotoImage(file="./back.png")
label_for_image = Label(root,image=image1)
label_for_image.place(x=-5, y=-2)

EmailVar = StringVar()
SubjectVar = StringVar()

def Clear():
    EmailVar.set("")
    SubjectVar.set("")
    t1.delete('1.0',END)
    
    e1.insert(0,"Enter client email address")
    e1.bind("<FocusIn>",lambda args: e1.delete("0",'end'))
    
    e2.insert(0,"Enter subject")
    e2.bind("<FocusIn>",lambda args: e2.delete("0",'end'))
    
    t1.insert(END,"Enter message")
    t1.bind("<FocusIn>",lambda args: t1.delete("1.0",END))

def Send():
    emailVar = EmailVar.get()
    subjectVar = SubjectVar.get()
    Msg = t1.get('1.0',END)
    print(emailVar,subjectVar,Msg)

Label(root,text="Email",font=("Calibri",25),width=8).place(x=100,y=40)
e1 = Entry(root,font=("Calibri",25),width=25,bd=10,textvariable=EmailVar)
e1.place(x=280,y=32)

Label(root,text="Subject",font=("Calibri",25),width=8).place(x=100,y=100)
e2 = Entry(root,font=("Calibri",25),width=25,bd=10,textvariable=SubjectVar)
e2.place(x=280,y=92)

Label(root,text="Message",font=("Calibri",25),width=8).place(x=100,y=160)
t1 = Text(root,height=5,width=25,font=("Calibri",25),bd=10)
t1.place(x=280,y=152)

Button(root,text="Send",font=("Calibri",22),width=6,command=Send).place(x=340,y=385)
Button(root,text="Clear",font=("Calibri",22),width=6,command=Clear).place(x=500,y=385)

Clear()

root.mainloop()