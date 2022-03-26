# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 14:05:15 2021

@author: sarina
"""
import cv2

import numpy as numpy
#import lbph as lr
import os,time
import sys
import msvcrt
import pathlib
from openpyxl import Workbook
import register
import csv

import creating_directory as cdir
 
def TakeImage(id, name, faculty, batch, email):
    print(id)
    print(name)
    print(faculty)
    print(batch)
    print(email)

    #directory "image"
    #directory for image storing
    
    img_dir = 'image database'
    #creatingdirectory function call garera image ra  faculty koo folder banako 
    path0=cdir.creatingdir(img_dir,faculty)
    #creatingdirectory function call garera batch koo folder banako 
    path1 = cdir.creatingbatchdir(path0, batch) 
     #creatingdirectory function call garera id_name koo folder banako 
    path2= cdir.creatingpersondir(path1, name,id)
    
    #information database info_db\faculty\batch.xslx file
    info_dir = "information database"
    path1_info = cdir.creatingdir(info_dir,faculty) #yeti samma chahi info\csit banxa
    #......excel save creation and sacing the informatiiom................

    
    file_name_new = batch+".csv"
    filejoinnew = os.path.join(path1_info,file_name_new)
    columns = ['ID', 'Name', 'Faculty', 'Batch', 'Email']
    serial = 0
    exists = os.path.isfile(filejoinnew)
    if exists:
        with open(filejoinnew, 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
               serial = serial + 1
            serial = (serial // 2)
            csvFile1.close()
    else:
        with open(filejoinnew, 'a',newline="") as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
            #serial = 1
            csvFile1.close()
        row = [id,name,faculty,batch,email]
        with open(filejoinnew, 'a',newline="") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        print("hhhhh")
    """
    excelfile_name=batch +".xlsx"
    file1=pathlib.Path(path1_info,excelfile_name)
    if file1.exists():
        print("file Exist")
    else:
        file= Workbook()
        sheet= file.active
        sheet["A1"]= "ID"
        sheet["B1"]= "Name"
        sheet["C1"]= "Faculty"
        sheet["D1"]= "Batch"
        sheet["E1"]= "Email"
        excelfile=os.path.join(path1_info,excelfile_name)
        file.save(excelfile)        
    
    
    
    path0=os.path.join(fn_dir)
    if not os.path.isdir(path0):
        os.mkdir(path0)
    
    #folder for faculty
    
    path = os.path.join(fn_dir, faculty)#/image1/faculty_name
    if not os.path.isdir(path):
        os.mkdir(path)
        
    #for batch folder
    path1=os.path.join(path, batch)
    if not os.path.isdir(path1):
        os.mkdir(path1)
    #for name folder
    path2=os.path.join(path1, name)
    if not os.path.isdir(path2):
        os.mkdir(path2)
"""
    
#---------------------detection starts and saving the image--------------------  
    
    
    count = 0
    size = 4
   
    
    (im_width, im_height) = (68, 68)
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    cap = cv2.VideoCapture(0)
    while count < 64:
        ret, im = cap.read()
        im = cv2.flip(im, 1, 0)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        mini = cv2.resize(gray, ((int)(gray.shape[1] / size), (int)(gray.shape[0] / size)))
        faces = face_cascade.detectMultiScale(mini)
        faces = sorted(faces, key=lambda x: x[3])
        if faces:
            face_i = faces[0]
            (x, y, w, h) = [v * size for v in face_i]
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (im_width, im_height))
            
            pin = sorted([int(n[:n.find('.')]) for n in os.listdir(path2)
                    if n[0]!='.' ]+[0])[-1] + 1
            cv2.imwrite('%s/%s.png' % (path2, pin), face_resize)
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
            
            time.sleep(0.38)        
            count += 1
                           
                                
            cv2.imshow('OpenCV', im)
            key = cv2.waitKey(10)
            if key == 27:
                break
    cv2.destroyAllWindows()
    cap.release()  
  
   