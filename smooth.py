import cv2 as cv
import numpy as np


img=cv.imread('E:\Downloads\Documents\open cv\code\im1.jpg')
# cv.imshow('img',img)
imgg=cv.resize(img,(500,500)) #without considering the aspect ratio
cv.imshow('resized',imgg)

# average blur
average=cv.blur(imgg,(3,3))
cv.imshow('average',average)

# gaussian blur
gauss=cv.GaussianBlur(imgg,(3,3),0)
cv.imshow('gaussian blur',gauss)

# median blur
median=cv.medianBlur(imgg,3)
cv.imshow('median',median)

# Bilateral blur
bilateral=cv.bilateralFilter(imgg,10,25,35)
cv.imshow('bilateral',bilateral)

cv.waitKey(0)