# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 18:41:51 2019

@author: Aditya
"""

#import all libraries
import cv2
import matplotlib.pyplot as plt

#Loading the image(In my case MSD image)
img = cv2.imread('MSDhoni.jpg',3)

#Converting to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#To convert BGR image to RGB image(Since we know that OpenCV loads an image in BGR format, so we need to convert it into RBG format to be able to display its true colors)
def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#pre-trained classifiers
haar_cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#TO dectect the face co-ordinate (function will return a rectangle with coordinates(x,y,w,h))
faces_rects = haar_cascade_face.detectMultiScale(img_gray, scaleFactor = 1.2, minNeighbors = 5);

# Let us print the no. of faces found
print('Faces found: ', len(faces_rects))

for (x,y,w,h) in faces_rects:
     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

#convert image to RGB and show image
plt.imshow(convertToRGB(img))


