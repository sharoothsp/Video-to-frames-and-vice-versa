# -*- coding: utf-8 -*-
"""
Created on Sat May  8 03:50:26 2021

@author: user
"""

import cv2
import numpy as np
#import glob

#to stores frames
img_array = []

#to split frame from video
vid = cv2.VideoCapture('bikeride.mp4')
success, img = vid.read()

c = 1
label =  "Video made"
font = cv2.FONT_HERSHEY_PLAIN
color = (255, 0, 0)

while success:
    cv2.putText(img, label,(20,20),font, 1, color, 3)
    #saving image in folder
    cv2.imwrite('video_frame\image_%d.jpg' % c, img)
    #saving image in array 
    img_array.append(img)
    height, width , layers = img.shape
    success, img = vid.read()
    print("saving image",c)
    c=c+1
    

#to make video from image 


    
fourcc = cv2.VideoWriter_fourcc(*'mp4v')    
out=cv2.VideoWriter('updated2.mp4', fourcc, 15, (width, height)) 


for i in range(len(img_array)):
    out.write(img_array[i])
out.release()


#to show video 
for i in range(len(img_array)):
    
    cv2.imshow('Frame',img_array[i])
    cv2.waitKey(5)

cv2.destroyAllWindows() 

"""
to read image from file 
img_array = []
for filename in glob.glob('video_frame\*.jpg'):
    img = cv2.imread(filename)
    
    img_array.append(img)

"""