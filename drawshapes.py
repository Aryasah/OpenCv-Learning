import cv2 as cv
import numpy as np
# img=cv.imread('images\leaf.jpg')
# cv.imshow('image',img)
# cv.waitKey(0)
# creating a blank image 
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)

# paint a image
blank[200:300, 300:400]=0,245,0

#draw a rectangle
cv.rectangle(blank,(0,0),(250,240),(255,34,0),-1)

#draw a circle
cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),80,(0,34,89),-1)

#draw a line
cv.line(blank,(blank.shape[0]//2,blank.shape[1]//2),(blank.shape[0]//3,blank.shape[1]//4),(0,345,13),5)

#write text
cv.putText(blank,'hello this is arya sah',(0,100),cv.FONT_HERSHEY_COMPLEX_SMALL,1.2,(123,400,12),3)
cv.imshow('blank',blank)


cv.waitKey(0)
