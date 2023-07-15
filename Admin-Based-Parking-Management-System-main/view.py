from tkinter import *
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox

def pos():
    root.destroy()
    os.system('python login.py')
    
def clse():
    root.destroy()
    os.system('python option.py')



        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("Parking")
    root.configure(bg='#FFC0CB')
    # label=Label(root,text="VEHICLE DETAILS",font="bold",fg="Red")
    # label.place(x=363,y=50)
    Name=[]
    Vno=[]
    Tno=[]
    Dater=[]
    vehi=[]
    norecord = 0
    f1 = open('twowheel.txt', 'r')
    for line in f1:
        norecord += 1
        line = line.rstrip('\n')
        word = line.split('|')
        Name.append(word[0])
        Vno.append(word[1])
        Tno.append(word[2])
        Dater.append(word[3])
        vehi.append('Two wheeler')
    f1.close()
    f1 = open('threewheel.txt', 'r')
    for line in f1:
        norecord += 1
        line = line.rstrip('\n')
        word = line.split('|')
        Name.append(word[0])
        Vno.append(word[1])
        Tno.append(word[2])
        Dater.append(word[3])
        vehi.append('Three wheeler')
    f1.close()
    f1 = open('fourwheel.txt', 'r')
    for line in f1:
        norecord += 1
        line = line.rstrip('\n')
        word = line.split('|')
        Name.append(word[0])
        Vno.append(word[1])
        Tno.append(word[2])
        Dater.append(word[3])
        vehi.append('Four wheeler')
    f1.close()
    f1 = open('other.txt', 'r')
    for line in f1:
        norecord += 1
        line = line.rstrip('\n')
        word = line.split('|')
        Name.append(word[0])
        Vno.append(word[1])
        Tno.append(word[2])
        Dater.append(word[3])
        vehi.append('Other')
    f1.close()
    borrow_list=Listbox(root,height=50,width=30)
    borrow_list1=Listbox(root,height=50,width=30)
    borrow_list2=Listbox(root,height=50,width=30)
    borrow_list3=Listbox(root,height=50,width=30)
    borrow_list4=Listbox(root,height=50,width=30)
    for num in range(0,norecord):
        borrow_list.insert(0,Name[num])
        borrow_list1.insert(0,Vno[num])
        borrow_list2.insert(0,Tno[num])
        borrow_list3.insert(0,Dater[num])
        borrow_list4.insert(0,vehi[num])
    borrow_list.configure(background="light grey")
    borrow_list1.configure(background="pink")
    borrow_list2.configure(background="light grey")
    borrow_list3.configure(background="pink")
    borrow_list4.configure(background="light grey")

    borrow_label=Label(root,text="Name")
    borrow_label2=Label(root,text="Vehicle No")
    borrow_label3=Label(root,text="Tocken")
    borrow_label4=Label(root,text="Date")
    borrow_label5=Label(root,text="Vehicle Type")

    borrow_label.grid(row=3,column=0)
    borrow_label2.grid(row=3,column=1)
    borrow_label3.grid(row=3,column=4)
    borrow_label4.grid(row=3,column=7)
    borrow_label5.grid(row=3,column=10)

    borrow_list.grid(row=4,column=0)
    borrow_list1.grid(row=4,column=1)
    borrow_list2.grid(row=4,column=4)
    borrow_list3.grid(row=4,column=7)
    borrow_list4.grid(row=4,column=10)

    b3=Button(root,text="Back",command=clse,bg="#68BBE3",activebackground="red",width=30)
    b3.place(x=700,y=420)
    root.mainloop()

