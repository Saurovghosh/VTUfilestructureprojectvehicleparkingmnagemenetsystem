from tkinter import *
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox
import dele
def clse():
    root.destroy()
    os.system('python option.py')

def ver():
    a=0
    if not vno.get():
        messagebox.showwarning("Warning","Fill the blank spaces.")
        a=1
    return a


# def delete_patient():
#     if not op.get():
#         messagebox.showwarning("Warning","Fill the blank spaces.")
#     else:
#         dele.pos(op.get())
        
#         messagebox.showwarning("Succes","Deleted Successfully.")

def ser():
    t=ver()
    if (t==0):
        f=open("twowheel.txt")
        lines = f.readlines()
        f.close()
        for i in lines:
            if i.find(vno.get())!=-1:
                li=[]
                li=i.split('|') 
                li.append('Two wheeler')
                for j in li:
                    t1.insert(END,j+"\n")   

        f=open("threewheel.txt")
        lines = f.readlines()
        f.close()
        for i in lines:
            if i.find(vno.get())!=-1:
                li=[]
                li=i.split('|') 
                li.append('Three wheeler')  
                for j in li:
                    t1.insert(END,j+"\n") 

        f=open("fourwheel.txt")
        lines = f.readlines()
        f.close()
        for i in lines:
            if i.find(vno.get())!=-1:
                li=[]
                li=i.split('|')   
                li.append('Four wheeler')
                for j in li:
                    t1.insert(END,j+"\n")  

        f=open("other.txt")
        lines = f.readlines()
        f.close()
        for i in lines:
            if i.find(vno.get())!=-1:
                li=[]
                li=i.split('|') 
                li.append('Other')  
                for j in li:
                    t1.insert(END,j+"\n")            





        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("Parking")
    root.configure(bg='#FFC0CB')

   
    label=Label(root,text="SEARCH",font="bold",fg="Red")
    label.place(x=450,y=50)

    vno=StringVar()


    label2=Label(root,text="Vehicle No:")
    label2.place(x=300,y=170)





    e2=Entry(root,textvariable=vno,width=40)
    e2.place(x=420,y=170)

   
    b4=Button(root,text="Search",command=ser,activebackground="red",bg="#68BBE3",width=30)
    b4.place(x=363,y=240)
    t1=Text(root,width=80,height=10)
    t1.place(x=10,y=280)
    b3=Button(root,text="Back",command=clse,bg="#68BBE3",activebackground="red",width=30)
    b3.place(x=700,y=420)
    root.mainloop()

