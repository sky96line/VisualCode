import cv2
import numpy as np

'''
cap = cv2.VideoCapture('http://192.168.43.56:8080/viewers.html#webcamxp')

while True:
  ret, frame = cap.read()
  cv2.imshow('frame', frame)
  
  if cv2.waitKey(1):
    break

cap.release()
cv2.destroyAllWindows()
'''
img = cv2.imread('pp.jpg',0)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()