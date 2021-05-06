import cv2 as cv

imag=cv.imread('pmo.jpg')
img=cv.resize(imag,(700,600)) #without considering the aspect ratio
cv.imshow('resized',img)

cv.imshow('image',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

haar_cascade =cv.CascadeClassifier('haar_face.xml')

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)

print(f'number of faces found{len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    img = cv.rectangle(img,(x,y),(x+w,y+h),(90,250,100),4)

cv.imshow('img',img)
cv.waitKey(0)