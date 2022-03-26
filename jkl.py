# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 10:13:16 2021

@author: sarina
"""

from PIL import Image

def get_num_pixels(filepath):
    width, height = Image.open(filepath).size
    return width*height

print(get_num_pixels("1.jpg"))