# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 18:03:54 2022

@author: Dell
"""
import cv2
import numpy as numpy
#import lbph as lr
import os,time
import sys
import msvcrt

count = 0
size = 4
fn_haar = 'haarcascade_frontalface_default.xml'
fn_dir = 'database'
fn_name = input('Enter Name Of The Person : ')   #name of the person
"""
#trying to create directory if it does not exist
dirr = 'parent'
path1 = os.path.join(dirr,fn_name)
if not os.path.isdir(dirr):
    os.mkdir(dirr)
 """    
path = os.path.join(fn_dir, fn_name) 
if not os.path.isdir(path):
    os.mkdir(path)
(im_width, im_height) = (68, 68)
haar_cascade = cv2.CascadeClassifier(fn_haar)
webcam = cv2.VideoCapture(0)


print("-----------------------Taking pictures----------------------")
print("--------------------Give some expressions---------------------")
# The program loops until it has 20/64 images of the face.
while count < 64:
    (rval, im) = webcam.read()
    im = cv2.flip(im, 1, 0)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    mini = cv2.resize(gray, ((int)(gray.shape[1] / size), (int)(gray.shape[0] / size)))
    faces = haar_cascade.detectMultiScale(mini)
    faces = sorted(faces, key=lambda x: x[3])
    if faces:
        face_i = faces[0]
        (x, y, w, h) = [v * size for v in face_i]
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (im_width, im_height))
        pin=sorted([int(n[:n.find('.')]) for n in os.listdir(path)
                    if n[0]!='.' ]+[0])[-1] + 1
        cv2.imwrite('%s/%s.png' % (path, pin), face_resize)
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(im, fn_name, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN,
                                    1,(0, 255, 0))
        time.sleep(0.38)        
        count += 1
                           
                                
        cv2.imshow('OpenCV', im)
        key = cv2.waitKey(10)
        if key == 27:
            break
print(str(count) + " images taken and saved to " + fn_name +" folder in database ")


#training
(images, lables, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(fn_dir):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(fn_dir, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            lable = id
                                    
            #original
            images.append(cv2.imread(path, 0))
            lables.append(int(lable))
        id += 1
(im_width, im_height) = (68, 68)
print(lables)
                        
                        
cv2.destroyAllWindows()
webcam.release()