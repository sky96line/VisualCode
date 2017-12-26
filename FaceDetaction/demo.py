import cv2
import numpy as np
import os

def get_files(root, files_of_type):
  rv = []
  for cwd, folders, files in os.walk(root):
    for fname in files:
      if os.path.splitext(fname)[1] in files_of_type:
        rv.append(cwd+'/'+fname)
  return rv

face_case = cv2.CascadeClassifier('objectDitection/face.xml')

files = get_files('Justin',['.jpg'])

i = int(get_last_file('Faces', ['.jpg']).split('-')[1].split('.')[0]) + 1
j = 1
for file in files:
  img = cv2.imread(file,0)
  faces = face_case.detectMultiScale(img, 1.3, 3)

  for x, y, w, h in faces:
    region = img[y:y + h, x:x + w]
    new_img = cv2.imwrite("Faces//face-" + str(i) + "." + str(j) + ".jpg", region)
    j+=1
  #imS = cv2.resize(img, (960, 540))
  #cv2.imshow('Image', img)
  #cv2.waitKey(1)
  #cv2.destroyWindow('Image')
