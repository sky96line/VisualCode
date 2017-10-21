from __future__ import print_function
import numpy as np
openSet = []
closeSet = []

start = [[1,2,3],[4,5,6],[7,8,0]]
goal = [[1,2,3],[4,6,5],[7,8,0]]

def display(state):
  for i in state:
    for j in i:
      print(j, end=" ")
    print()

def getIndex(state, elemant):
  for i in range(3):
    for j in range(3):
      if state[i][j] is elemant:
        return i,j

def possibleMoves(state):
  i,j = getIndex(state,0)
  print(i,j)
  tempUp = state
  tempDown = state
  tempLeft = state
  tempRight = state

  tempUp[i][j], tempUp[i - 1][j] = tempUp[i - 1][j], tempUp[i][j]
  if tempUp not in closeSet:
    print('up')
    openSet.append(tempUp)
    closeSet.append(tempUp)
    possibleMoves(tempUp)

  tempDown[i][j], tempDown[i + 1][j] = tempDown[i + 1][j], tempDown[i][j]
  if tempDown not in closeSet:
    print('down')
    openSet.append(tempDown)
    closeSet.append(tempDown)
    possibleMoves(tempDown)

  tempRight[i][j], tempRight[i][j - 1] = tempRight[i][j - 1], tempRight[i][j]
  if tempRight not in closeSet:
    print('right')
    openSet.append(tempRight)
    closeSet.append(tempRight)
    possibleMoves(tempRight)

  tempLeft[i][j], tempLeft[i][j + 1] = tempLeft[i][j + 1], tempLeft[i][j]
  if tempLeft not in closeSet:
    print('left')
    openSet.append(tempLeft)
    closeSet.append(tempLeft)
    possibleMoves(tempLeft)

openSet.append(start)
while openSet:
  s = openSet.pop()
  if s is goal:
    break
  #display(s)
  possibleMoves(s)
