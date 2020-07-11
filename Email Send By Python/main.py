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

def Send():
    emailVar = EmailVar.get()
    subjectVar = SubjectVar.get()
    Msg = t1.get('1.0',END)
    print(emailVar,subjectVar,Msg)

Label(root,text="Email",font=("Calibri",25),width=8).place(x=100,y=40)
Entry(root,font=("Calibri",25),width=25,bd=10,textvariable=EmailVar).place(x=280,y=32)

Label(root,text="Subject",font=("Calibri",25),width=8).place(x=100,y=100)
Entry(root,font=("Calibri",25),width=25,bd=10,textvariable=SubjectVar).place(x=280,y=92)

Label(root,text="Message",font=("Calibri",25),width=8).place(x=100,y=160)
t1 = Text(root,height=5,width=25,font=("Calibri",25),bd=10)
t1.place(x=280,y=152)

Button(root,text="Send",font=("Calibri",22),width=6,command=Send).place(x=340,y=385)
Button(root,text="Clear",font=("Calibri",22),width=6).place(x=500,y=385)

root.mainloop()