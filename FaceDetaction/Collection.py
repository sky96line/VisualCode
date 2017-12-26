import cv2
import numpy as np
import os

def get_last_file(root, files_of_type):
  rv = None
  for cwd, folders, files in os.walk(root):
    for fname in files:
      if os.path.splitext(fname)[1] in files_of_type:
        rv=fname
  return rv

#i = int(get_last_file('Faces', ['.jpg']).split('-')[1].split('.')[0]) + 1
i = 1
j = 1

img = cv2.imread('Justin/29-FaceId-0.jpg')
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_case = cv2.CascadeClassifier('objectDitection/face.xml')
faces = face_case.detectMultiScale(img,1.7,5) # (img, 1.7, 5) for g.jpg; (1.1,3 for gg.jpg)

eye_case = cv2.CascadeClassifier('objectDitection/eye.xml')
eyes = eye_case.detectMultiScale(img,1.7,5)

for x, y, w, h in faces:
  region = img[y:y+h,x:x+w]
  cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
  #new_img = cv2.imwrite("Faces//face-" + str(i) + "." + str(j) + ".jpg", region)
  break

imS = cv2.resize(img, (960, 540))
cv2.imshow('Image', imS)
cv2.waitKey(0)
cv2.destroyAllWindows()
