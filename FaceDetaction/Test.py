import os
import numpy as np
import cv2 as cv
import pickle
from sklearn.neural_network import MLPClassifier

def getName(TARGET):
  f = open('Data.txt', 'r')
  names = f.read()
  names = names.split('\n')
  for chk in names[:-1]:
    if(TARGET == int(chk[0])):
      return chk[2:]
  return 'Not Found'

img_check = cv.imread('Media/amita0.jpg', 0)

img_check = np.asarray(img_check)
h, w = img_check.shape
img_check = img_check.reshape(w * h)

with open('Classifier/clf.pkl', 'rb') as f:
    clf = pickle.load(f)

p = clf.predict([img_check])

name = getName(p)
print name