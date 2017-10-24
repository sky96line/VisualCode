import cv2
import numpy as np

cap = cv2.VideoCapture('poc')

while True:
  ret, frame = cap.read()
  cv2.imshow('frame', frame)
  
  if cv2.waitKey(1):
    break

cap.release()
cv2.destroyAllWindows()
'''
img = cv2.imread('pp.jpg')

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''