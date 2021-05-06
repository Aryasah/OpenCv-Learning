import cv2 as cv 
import numpy as np

img=cv.imread('E:\Downloads\Documents\open cv\images\leaf.jpg')
#translate an image 
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)
#rotate an image
def rotate(img,angle,rotpoint=None):
    (height,width)=img.shape[:2]
    if rotpoint is None:
        rotpoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rotate=rotate(img,45)
cv.imshow('rotated',rotate)
translate=translate(img,--100,100)
cv.imshow('translate',translate)
cv.waitKey(0)

