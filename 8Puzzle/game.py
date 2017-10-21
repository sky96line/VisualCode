import numpy as np
start = [[1,2,3],[4,5,6],[7,8,0]]

def get(state, element):
  for i in range(3):
    for j in range(3):
      if state[i][j] is element:
        return i,j

x,y = get(start, 0)
print(x,y)