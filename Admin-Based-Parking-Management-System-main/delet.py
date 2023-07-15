from tkinter import *
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox
import dele
def clse():
    root.destroy()
    os.system('python option.py')



def delete_vehicle():
    if not tno.get():
        messagebox.showwarning("Warning","Fill the blank spaces.")
    else:
        dele.pos(vno.get(),tno.get(),menu.get())
        
        messagebox.showwarning("Succes","Checkout completed.")

        

                    





        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("Parking")
    root.configure(bg='#FFC0CB')

   
    label=Label(root,text="CHECKOUT",font="bold",fg="Red")
    label.place(x=420,y=50)

    tno=StringVar()
    vno=StringVar()
    menu= StringVar()
    menu.set("Select Vehicle Type")

    #Create a dropdown Menu
    drop= OptionMenu(root, menu,"TwoWheeler", "ThreeWheeler","FourWheeler","Others")

    drop.pack()
    drop.place(x=400,y=100)

    label2=Label(root,text="Tocken No:")
    label2.place(x=300,y=170)
    label2=Label(root,text="Vehicle No:")
    label2.place(x=300,y=220)





    e2=Entry(root,textvariable=tno,width=40)
    e2.place(x=420,y=170)
    e2=Entry(root,textvariable=vno,width=40)
    e2.place(x=420,y=220)

   
    b4=Button(root,text="Checkout",command=delete_vehicle,activebackground="red",bg="#68BBE3",width=30)
    b4.place(x=363,y=300)
    b3=Button(root,text="Back",command=clse,bg="#68BBE3",activebackground="red",width=30)
    b3.place(x=700,y=420)
    root.mainloop()

