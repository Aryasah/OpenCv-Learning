import cv2 as cv 
import numpy as np

img=cv.imread('E:\Downloads\Documents\open cv\code\im1.jpeg')
cv.imshow('image',img)

cropped=cv.resize(img,(500,600)) #without considering the aspect ratio
cv.imshow('resized',cropped)

# cropped=img[300:800,0:700]
# cv.imshow('image',cropped)

gray=cv.cvtColor(cropped,cv.COLOR_BGR2GRAY)
cv.imshow('image',gray)

blur=cv.GaussianBlur(cropped,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

canny=cv.Canny(cropped,125,175)
cv.imshow('canny',canny)

# ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
# cv.imshow('tres',thresh)

blank=np.zeros(img.shape,dtype='uint8')
contours,heirarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))
cv.drawContours(blank,contours,-1,(255,120,0),1)
cv.imshow('contoress',blank)

cv.waitKey(0)