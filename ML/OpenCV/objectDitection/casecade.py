import cv2
import numpy as np

face_case = cv2.CascadeClassifier('face.xml')

eye_case = cv2.CascadeClassifier('eye.xml')

car_case = cv2.CascadeClassifier('cars.xml')

plat_case = cv2.CascadeClassifier('licence_plate.xml')

img = cv2.imread('imgs/car1.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_case.detectMultiScale(gray,2, 5)
for x, y, w, h in faces:
  cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

eyes = eye_case.detectMultiScale(gray,1.3, 5)
for x, y, w, h in eyes:
  cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cars = car_case.detectMultiScale(gray, 1.3, 5)
for x, y, w, h in cars:
  cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

plats = plat_case.detectMultiScale(gray, 1.3, 5)
for x, y, w, h in plats:
  cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()