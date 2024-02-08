#tkinter is a gui which cannot take more power

#1.import the libraries
from tkinter import *
from tkinter import messagebox
import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="kritika"
)

#2.create main application window/root
root = Tk()
root.geometry("400x500")
#Tk stands for toolkit

#3.adding widgets and widgets are icons
#syntax
#widgets(mainwindow,options/parameters)
#widgets are always starts with  capital letter

#form
lbl =Label(root,text="firstname").place(x=0,y=1)
ent1=Entry(root)
ent1.place(x=70,y=1)

lbl2= Label(root,text="rollno").place(x=0,y=25)
ent2=Entry(root)
ent2.place(x=70,y=25)

#lbl3=Label(root,text="mobile number").place(x=0,y=50)
#ent3=Entry(root)
#ent3.place(x=90,y=50)

#lbl4=Label(root,text="address").place(x=0,y=80)
#ent4=Entry(root)
#ent4.place(x=50,y=80)

def func():
    #fteching values from the form
    name = ent1.get()
    rollno = ent2.get()
    #inserting values in the table
    insert = """insert into students(student_name,rollno)value(%s,%s)"""
    values=(name,rollno)
    
    #messagebox.showinfo("messagebox","record collected")
    #messagebox.showerror("messagebox",".exe error")
    #messagebox.showwarning("messagebox","danger ahead")
    #messagebox.askokcancel("title","hello there!")
    
    #executing the values
    cursor=conn.cursor()
    cursor.execute(insert,values)
    conn.commit()
    messagebox.showinfo("title","records collected")
    conn.close()
    



btn=Button(root,text='submit',bg="green",foreground="white",activebackground="red",activeforeground="white",height=5,width=10,command=func).place(x = 100,y=200)

#4.calling the main window
root.mainloop() 

#three types of geometry
#1.Pack(side) 2.Place(xaxis/yaxis) 3.Grid(row,column)