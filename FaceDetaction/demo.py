import cv2
import numpy as np
import os


face_case = cv2.CascadeClassifier('objectDitection/face.xml')
'''
cap = cv2.VideoCapture('mm.wmv')

while True:
  ret, frame = cap.read()
  cv2.imshow('frame', frame)

  if(cv2.waitKey(30) >= 0):
    break
  
cap.release()
cv2.destroyAllWindows()
'''
img = cv2.imread('pp.jpg')

faces = face_case.detectMultiScale(img, 1.1, 3)#(img, 1.7, 5) for g.jpg

onlyfiles = next(os.walk('Faces/'))[2]  # dir is your directory path as string
i = len(onlyfiles)

for x, y, w, h in faces:
  region = img[y:y+h,x:x+w]
  new_img = cv2.imwrite("Faces//face-"+str(i)+".jpg",region)
  cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
  i+=1

imS = cv2.resize(img, (960, 540))
cv2.imshow('Image', imS)
cv2.waitKey(0)
cv2.destroyAllWindows()
