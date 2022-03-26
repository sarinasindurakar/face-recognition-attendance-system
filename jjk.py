# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 09:37:56 2021

@author: sarina
"""

import image
def getbinaryString( value , threshold):
        if value>=threshold:
            return 1
        else:
           return 0

def GetImageSize(img image.Image):
    if img==nil:
        return 0,0
    width,heigth=img.shape;
    