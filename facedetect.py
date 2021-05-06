import cv2 as cv
import numpy as np


img=cv.imread('group2.jpg')
resize=cv.resize(img,(500,500))


gray=cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)



haar_cascade=cv.CascadeClassifier('haar_face.xml')

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
for (x,y,w,h) in faces_rect:
    resize = cv.rectangle(resize,(x,y),(x+w,y+h),(20,170,60),2)
 

cv.imshow('img',resize)

cv.waitKey(0)