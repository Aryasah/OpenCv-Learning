import cv2 as cv 
import numpy as np


img=cv.imread('E:\Downloads\Documents\open cv\images\scene.jpg')
# cv.imshow('image',img)

def rescaleFrame(frame,scale=0.05):
    width=int(frame.shape[0]*0.15)
    height=int(frame.shape[1]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
#rescaling image
frameresized=rescaleFrame(img) 
cv.imshow('frameresized',frameresized)

#grayscaling
gray=cv.cvtColor(frameresized,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#blur
blur=cv.GaussianBlur(frameresized,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#curvetracing
canny=cv.Canny(blur,125,175)
cv.imshow('canny',canny)
#dilation of image
dilated=cv.dilate(canny,(3,3),iterations=1)
cv.imshow('dilated',dilated)
#eroding to get cascaded image back
eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow('ereoded image',eroded)
#resizing an image
resize=cv.resize(img,(500,500)) #without considering the aspect ratio
cv.imshow('resized',resize)

resize=cv.resize(img,(500,500),interpolation=cv.INTER_AREA) 
cv.imshow('resized',resize)

resize=cv.resize(frameresized,(1000,700),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resize)

#croping an image
cropped=frameresized[50:200,300:500]
cv.imshow('cropped',cropped)

cv.waitKey(0)