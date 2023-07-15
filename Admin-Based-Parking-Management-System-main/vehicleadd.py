from tkinter import *
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox
def clse():
    root.destroy()
    os.system('python option.py')


def verifier():
    a=b=c=d=0
    if not menu.get():
        #t1.insert(END,"<>Name is required<>\n")
        a=1
    if not name.get():
        #t1.insert(END,"<>Adhar no is required<>\n")
        d=1
    if not vno.get():
        #t1.insert(END,"<>Adhar no is required<>\n")
        b=1
    if not tno.get():
        #t1.insert(END,"<>Age is required<>\n")
        c=1
    
    if a==1 or b==1 or c==1 or d==1:
        messagebox.showwarning("Warning","Fill the blank spaces.")
        return 1
    else:
        return 0

def ad():
    if menu.get()=="TwoWheeler":
        t1=datetime.datetime.now()
        m1=t1.strftime("%Y:%m:%d")
        ls=name.get()+'|'+vno.get()+'|'+tno.get()+'|'+m1+"\n"
    
        p=open('twowheel.txt','a')
        read=open('twowheel.txt','r')
        if(read.__sizeof__() > 100):
            messagebox.showwarning("Warning", "Cannot add more vehicles in space")
            p.close()
            read.close()
        else:
            p.write(ls)
            messagebox.showwarning("Succes","Added Successfully.")
            p.close()
    
    if menu.get()=="ThreeWheeler":
        t1=datetime.datetime.now()
        m1=t1.strftime("%Y:%m:%d")
        ls=name.get()+'|'+vno.get()+'|'+tno.get()+'|'+m1+"\n"
    
        p=open('threewheel.txt','a')
        read=open('threewheel.txt','r')
        if(read.__sizeof__() > 100):
            messagebox.showwarning("Warning", "Cannot add more vehicles in space")
            p.close()
            read.close()
        else:
            p.write(ls)
            messagebox.showwarning("Succes","Added Successfully.")
            p.close()

    if menu.get()=="FourWheeler":
        t1=datetime.datetime.now()
        m1=t1.strftime("%Y:%m:%d")
        ls=name.get()+'|'+vno.get()+'|'+tno.get()+'|'+m1+"\n"
    
        p=open('fourwheel.txt','a')
        read=open('fourwheel.txt','r')
        if(read.__sizeof__() > 100):
            messagebox.showwarning("Warning", "Cannot add more vehicles in space")
            p.close()
            read.close()
        else:
            p.write(ls)
            messagebox.showwarning("Succes","Added Successfully.")
            p.close()

    if menu.get()=="Others":
        t1=datetime.datetime.now()
        m1=t1.strftime("%Y:%m:%d")
        ls=name.get()+'|'+vno.get()+'|'+tno.get()+'|'+m1+"\n"
    
        p=open('other.txt','a')
        read=open('other.txt','r')
        if(read.__sizeof__() > 100):
            messagebox.showwarning("Warning", "Cannot add more vehicles in space")
            p.close()
            read.close()
        else:
            p.write(ls)
            messagebox.showwarning("Succes","Added Successfully.")
            p.close()


def add_vehicle():
    ret=verifier()
    if ret==0:
        ad()

    
    


if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("Parking")
    root.configure(bg='#FFC0CB')
    
    menu= StringVar()
    menu.set("Select Vehicle Type")

    #Create a dropdown Menu
    drop= OptionMenu(root, menu,"TwoWheeler", "ThreeWheeler","FourWheeler","Others")

    drop.pack()
    drop.place(x=400,y=50)




    
    vno=StringVar()
    tno=StringVar()
    name=StringVar()
    label2=Label(root,text=" Name:")
    label2.place(x=300,y=120)

    label1=Label(root,text="Vehicle No:")
    label1.place(x=300,y=170)

    label2=Label(root,text="Tocken No:")
    label2.place(x=300,y=220)

    e1=Entry(root,textvariable=name,width=40)
    e1.place(x=420,y=120)

    e1=Entry(root,textvariable=vno,width=40)
    e1.place(x=420,y=170)

    e2=Entry(root,textvariable=tno,width=40)
    e2.place(x=420,y=220)

   
    b4=Button(root,text="Submit",command=add_vehicle,activebackground="pink",bg="#68BBE3",width=30)
    b4.place(x=363,y=420)


    b3=Button(root,text="Back",command=clse,bg="#68BBE3",activebackground="red",width=30)
    b3.place(x=700,y=420)
  
    
    root.mainloop()