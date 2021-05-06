import cv2 as cv
img=cv.imread('images/image.jpg')

cv.imshow('image',img)

def rescaleFrame(frame,scale=1.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
    
resized=rescaleFrame(img)
cv.imshow('image resized',resized)


cv.waitKey(0)

# capture=cv.VideoCapture('videos\kota.mp4')

# while(True):
#     Istrue, frame=capture.read()
#     frame_resized=rescaleFrame(frame)
#     cv.imshow('Video',frame)
#     cv.imshow('Video Resized',frame_resized)
#     if (cv.waitKey(20) & 0xFF==('d')):
#         break
    
capture.release
cv.destroyAllWindows()