from tkinter import *
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox
def clse():
    sys.exit() 
def pos():
    ret=verifier()
    if ret==0:
        h=open("admin.txt")
        lines = h.readlines()
        h.close()
        for i in lines:
            if i.find(eid.get())!=-1 and i.find(psw.get())!=-1:
                messagebox.showwarning("success","Authorization Success.")
                root.destroy()
                
                
                os.system('python option.py')
                break
        else:
            messagebox.showwarning("Warning","Embloyee id or password is incorrect.")
    else:
        messagebox.showwarning("Warning","Type Embloyee id and password.")
def verifier():
    a=b=0
    if not eid.get():
        a=1
    if not psw.get():
        b=1
    if a==1 or b==1 :
        return 1
    else:
        return 0  
        


                  




        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("Parking")
    root.configure(bg='#FFC0CB')
    

    eid=StringVar()
    psw=StringVar()
    label=Label(root,text="LOGIN",font="bold",fg="Red")
    label.place(x=450,y=50)
    label1=Label(root,text="Embloyee id :")
    label1.place(x=360,y=120)

    label2=Label(root,text="Password      :")
    label2.place(x=360,y=150)


    e1=Entry(root,textvariable=eid)
    e1.place(x=460,y=120)

    e2=Entry(root,show='*',textvariable=psw)
    e2.place(x=460,y=150)
   
    b4=Button(root,text="Submit",command=pos,activebackground="pink",bg="#68BBE3",width=30)
    b4.place(x=363,y=200)
    b3=Button(root,text="Close",command=clse,bg="#68BBE3",activebackground="red",width=30)
    b3.place(x=700,y=420)
    root.mainloop()

