import cv2
import numpy as np

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
rec = cv2.createEigenFaceRecognizer(15,3000)

faces = face_case.detectMultiScale(img, 1.1, 3)#(img, 1.7, 5) for g.jpg

i=34
for x, y, w, h in faces:
  region = img[y:y+h,x:x+w]
  new_img = cv2.imwrite("face-"+str(i)+".jpg",region)
  #cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
  i+=1

imS = cv2.resize(img, (960, 540))
cv2.imshow('Image', imS)
cv2.waitKey(0)
cv2.destroyAllWindows()
