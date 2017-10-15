from __future__ import print_function

start = [[1,2,3], [4,6,5], [7,8,0]]
goal = [[1,2,3], [8,0,4],[7,6,5]]

def display(state):
  for i in state:
    for j in i:
      print(j, end=" ")
    print()

def getIndex(state, goal):
  for i in range(3):
    for j in range(3):
      if state[i][j] is goal:
        yield i
        yield j
        break

def getHScore(state):
  HScore = 0
  for i in range(3):
    for j in range(3):
      elemant = state[i][j]
      a, b = getIndex(goal,elemant)
      HScore = HScore + abs(i-a) + abs(j-b)
  return HScore

def getGScore(state, prevG):
  GScore = 0
  for i in range(3):
    for j in range(3):
      if goal[i][j] is state[i][j]:
        GScore += 1
  return prevG + GScore

def getFScore(state, prevF):
  return getHScore(state) + getGScore(state, prevF)

print(getFScore(start,0))