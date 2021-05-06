import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('E:\Downloads\Documents\open cv\images\scene.jpg')
# cv.imshow('img',img)
imgg=cv.resize(img,(700,500)) #without considering the aspect ratio
cv.imshow('resized',imgg)

gray=cv.cvtColor(imgg,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])
plt.figure()
plt.title('Grayscalehistogram')
plt.xlabel('Bins')
plt.ylabel('no of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

blank=np.zeros(imgg.shape[:2],dtype='uint8')
circle=cv.circle(blank.copy(),(350,250),250,255,-1)

mask=cv.bitwise_and(imgg,imgg,mask=circle)
color=('b','g','r')
plt.figure()
plt.title('colorhistogram')
plt.xlabel('Bins')
plt.ylabel('no of pixels')
plt.xlim([0,256])
for i,col in enumerate(color):
    hist=cv.calcHist([imgg],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
plt.show()
cv.waitKey(0)