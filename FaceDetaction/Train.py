import os
import numpy as np
import cv2
import time
from PIL import Image

ID = int(raw_input('Enter ID : '))
def get_files(root, files_of_type):
  rv = []
  for cwd, folders, files in os.walk(root):
    for fname in files:
      if os.path.splitext(fname)[1] in files_of_type:
        rv.append(cwd+'/'+fname)
  return rv

eigenRecog = cv2.createEigenFaceRecognizer(15)

files = get_files('Faces', ['.jpg'])

faceList = []
IDs = []
for file in files:
  img = Image.open(file).convert('L')
  img = img.resize((110, 110))
  img = np.array(img)
  #cv2.imshow('ID : '+str(ID)+'-Face',img)
  imgNP = np.array(img,'uint8')
  
  faceList.append(imgNP)
  IDs.append(ID)

IDNP = np.array(IDs)

eigenRecog.train(faceList,IDNP)
eigenRecog.save('Recog/EigenFaceRecognizer.xml')