import cv2 as cv 
import numpy as np

img=cv.imread('pmo.jpg')
# cv.imshow('img',img)
imgg=cv.resize(img,(500,500)) #without considering the aspect ratio
cv.imshow('resized',imgg)
# # BGR TO  GRAY
gray=cv.cvtColor(imgg,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
# BGR to HUE
hue=cv.cvtColor(imgg,cv.COLOR_BGR2HSV)
cv.imshow('hue',hue)
# BGR to LAB
lab=cv.cvtColor(imgg,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)
#BGR to RGB
rgb=cv.cvtColor(imgg,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)


# COLOR CHANNELS
b,g,r=cv.split(imgg)
cv.imshow('BLUE',b)
cv.imshow('RED',r)
cv.imshow('GREEN',g)

#printing shapes 
print(img.shape)
print(r.shape)
print(g.shape)
print(b.shape)

#merging images
# merged=cv.merge([b,g,r])
# cv.imshow('merged',merged)

blank=np.zeros(imgg.shape[:2],dtype='uint8')
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow('BLUE',blue)
cv.imshow('RED',red)
cv.imshow('GREEN',green)



cv.waitKey(0)