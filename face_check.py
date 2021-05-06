import cv2 as cv 
import numpy as np
import os

p=[]
for i in os.listdir(r'E:\Downloads\Documents\open cv\code\train'):
    p.append(i)
print(p)

haar_cascade=cv.CascadeClassifier('haar_face.xml')
# features=np.load('features.npy' ,allow_pickle=True)
# labels=np.load('labels.npy')

face_recognizer =cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')
img=cv.imread(r'E:\Downloads\Documents\open cv\opencv-course-master\opencv-course-master\Resources\Faces\val\elton_john\3.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray unidentified',gray)


# facedetection
faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
i=20
for (x,y,w,h) in faces_rect:
    face_rol= gray[y:y+h,x:x+w]
    label,confidence=face_recognizer.predict(face_rol)
    print(f'p{label} with a confidence of {confidence}')
    cv.putText(img,str(p[label]),(20,i),cv.FONT_HERSHEY_COMPLEX,1.1,(0,240,200),2)
    img = cv.rectangle(img,(x,y),(x+w,y+h),(20,170,60),2)
    i=i+100

cv.imshow('detected face',img)
cv.waitKey(0)
