# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 18:03:53 2021

@author: sarina
"""

import tkinter as tk
import datetime 
import time
from PIL import Image, ImageTk
from tkinter import messagebox
import register
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

def register_fun():
   if messagebox.askyesno("Message","Have you registered already?") == True:
       print ("you can register")
       
   else:
       register.registerme() # file name register tesko vitra ko registerme function
       

#windows title
window.title("Attendance recognition system")
#windows stze
window.geometry("600x600")
window.resizable(False, False)


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


 


frame3=tk.Frame(window,width=200,height=100)
frame3.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
button =tk.Button(frame3, text="Register", fg="red",command=register_fun)
button.pack(padx=20,pady=20)

frame4=tk.Frame(window,width=200,height=100)
frame4.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
button1 =tk.Button(frame4, text="Take Attendance", fg="red")
button1.pack(padx=20,pady=20)

frame5=tk.Frame(window,width=200,height=100)
frame5.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
button2 =tk.Button(frame5, text="See details", fg="red")
button2.pack(padx=20,pady=20)

window.mainloop()