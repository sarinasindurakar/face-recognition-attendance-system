# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 09:02:21 2021

@author: sarina
"""

import tkinter as tk
import datetime 
import time
from PIL import Image, ImageTk
import facedetection
from tkinter import messagebox  
import re
def registerme():
    window=tk.Tk()
    

    def tick():
        time_string = time.strftime('%H:%M:%S')
        clock.config(text=time_string)
        clock.after(200,tick)

    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    day,month,year=date.split("-")
    
    mont={'01':'January',
          '02':'February',
          '03':'March',
          '04':'April',
          '05':'May',
          '06':'June',
          '07':'July',
          '08':'August',
          '09':'September',
          '10':'October',
          '11':'November',
          '12':'December'
          }
    def takeimage_full():
        id = txt_id.get()
        name = txt_name.get()
        faculty = txt_faculty.get()
        batch = txt_batch.get()
        email = txt_email.get()
        facedetection.TakeImage(id, name, faculty, batch, email);
   
    #windows title
    window.title("Register.Fill the form")
    #windows stze
    window.geometry("600x600")
    window.resizable(False, False)
    
    """
    
    #frame 1 is for image ie header
    frame1=tk.Frame(window,width=200,height=100,bg="red")
    frame1.pack(fill=tk.BOTH)
    image=Image.open("1.jpg")
    resize_img=image.resize((500,130),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(resize_img)
    h1=tk.Label(frame1,image=photo)
    h1.place(x=0,y=0,width=500,height=100)
    
    #image2
    image2=Image.open("2.jpg")
    resize_img2=image2.resize((500,130),Image.ANTIALIAS)
    photo2=ImageTk.PhotoImage(resize_img2)
    h2=tk.Label(frame1,image=photo2)
    h2.place(x=500,y=0,width=500,height=100)
    """
    
    #frame 2 is for title
    frame2=tk.Frame(window,width=200,height=100)
    frame2.pack(fill=tk.BOTH)
    message1 = tk.Label(frame2, text="Face Recognition Based Attendance System" ,fg="green" ,width=80,height=2,font=('times', 20, ' bold '))
    #message1.place(x=80,y=10)
    message1.pack()
    
    #date 
    datef = tk.Label(frame2, text = day+"-"+mont[month]+"-"+year+"   ", fg="orange" ,width=80 ,height=1,font=('times', 20, ' bold '))
    #datef.place(x=100,y=160)
    datef.pack()
    #time
    clock = tk.Label(frame2,fg="orange" ,width=80 ,height=1,font=('times', 20, ' bold '))
    #clock.place(x=100,y=200)
    clock.pack()
    tick()
    
    
    #--------------------------------registration part start---------------------------------------------
    
    frame3=tk.Frame(window,width=200,height=100)
    frame3.pack(fill=tk.BOTH)
    message2 = tk.Label(frame3, text="Registration Form" ,fg="green" ,width=80,height=2,font=('times', 20, ' bold '))
    #message1.place(x=80,y=10)
    message2.pack()
    
    #resgister ko lagi  frame
    
    frame4=tk.Frame(window,width=200,height=300,bg="yellow")
    frame4.pack(fill=tk.BOTH)
    
    #tkinter variable for storing entries
    
    
    #--------------------validation----------------------
    def validate(ID):
        if ID.isdigit():
            return True
        if len(str(ID))== 0:
            return True
        else:
            messagebox.showwarning("Invalid","Invalid Entry")
            return False
    
    my_valid = window.register(validate)
    
    lbl1= tk.Label(frame4, text="Enter ID",width=8  ,height=1  ,fg="black",font=('times', 17, ' bold ') )
    lbl1.place(x=140, y=55)
    txt_id = tk.Entry(frame4,width=20,fg="black",font=('times', 15, ' bold '),validate='key',validatecommand=(my_valid,'%S'))
    txt_id.place(x=280, y=55)
    
    def validate_name(name):#for ID and batch validation
        if name.isalpha():
            return True
        if name == "":
            return True	
        else:
            messagebox.showwarning("Invalid","Only Alphabet is allowed") 
            return False
    valid_name = window.register(validate_name)
    lbl2= tk.Label(frame4, text="Name",width=8 ,height=1  ,fg="black",font=('times', 17, ' bold ') )
    lbl2.place(x=140, y=90)
    
    txt_name = tk.Entry(frame4,width=20,fg="black",font=('times', 15, ' bold '),validate='key',validatecommand=(valid_name,'%P'))
    txt_name.place(x=280, y=90)
    
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    def email_validation(email):
        if(re.search(regex,email) and email.isalpha):
            return True 
        if email == "":
            return True	
        else:
            messagebox.showwarning("Alert","Invalid E-mail enter by user")
            return False
    my_validmail=window.register(email_validation)  
    
    lbl5= tk.Label(frame4, text="Email",width=8  ,height=1  ,fg="black",font=('times', 17, ' bold ') )
    lbl5.place(x=140, y=125)
    txt_email = tk.Entry(frame4,width=20,fg="black",font=('times', 15, ' bold '),validate='focusout',validatecommand=(my_validmail,'%P'))
    txt_email.place(x=280, y=125)
   
    lbl3= tk.Label(frame4, text="Faculty",width=8  ,height=1  ,fg="black",font=('times', 17, ' bold ') )
    lbl3.place(x=140, y=160)
    txt_faculty = tk.Entry(frame4,width=20,fg="black",font=('times', 15, ' bold '),validate='key',validatecommand=(valid_name,'%S'))
    txt_faculty.place(x=280, y=160)
    
    lbl4= tk.Label(frame4, text="Batch",width=8  ,height=1  ,fg="black",font=('times', 17, ' bold ') )
    lbl4.place(x=140, y=195)
    txt_batch = tk.Entry(frame4,width=20,fg="black",font=('times', 15, ' bold '),validate='key',validatecommand=(my_valid,'%S'))
    txt_batch.place(x=280, y=195)
    
    
    
    button_save =tk.Button(frame4, text="Take Image and Save",width="20",height="2", fg="red",command=takeimage_full)
    button_save.place(x=200,y=250)
    
    """
    
    button_save =tk.Button(frame4, text="Save Profile", width="10",height="2",fg="red",command=saveme)
    button_save.place(x=300,y=250)
    """
    
    
    
    
    window.mainloop();