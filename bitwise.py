import cv2 as cv
import numpy as np

img=cv.imread('E:\Downloads\Documents\open cv\images\scene.jpg')
# cv.imshow('img',img)
imgg=cv.resize(img,(700,500)) #without considering the aspect ratio
cv.imshow('resized',imgg)

blank=np.zeros(imgg.shape[:2],dtype='uint8')
rectangle=cv.rectangle(blank.copy(),(157,30),(550,450),255,-1)
cv.imshow('rectangle',rectangle)
circle=cv.circle(blank.copy(),(350,250),250,255,-1)
cv.imshow('circle',circle)
# # bitwise AND
# bitwise_and=cv.bitwise_and(rectangle,circle)
# cv.imshow('bitwise_and',bitwise_and)

# # bitwise OR
# bitwise_or=cv.bitwise_or(rectangle,circle)
# cv.imshow('bitwise_or',bitwise_or)

# #Bitwise NOT
# bitwise_not=cv.bitwise_not(rectangle,circle)
# cv.imshow('bitwise_not',bitwise_not) 

# masking
mask=cv.bitwise_and(imgg,imgg,mask=circle)
cv.imshow('mask',mask)




cv.waitKey(0)