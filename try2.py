# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 20:46:00 2021

@author: sarina
"""

import cv2
def TakeImage():
    (im_width, im_height) = (68, 68)
    haar_cascade = cv2.CascadeClassifier(fn_haar)
    webcam = cv2.VideoCapture(0)
    print("-----------------------Taking pictures----------------------")
    print("--------------------Give some expressions---------------------")
    # The program loops until it has 20 images of the face.
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