from __future__ import print_function
import math

start = [[2,8,3], 
         [1,6,4], 
         [0,7,5]]

curup = [[2,8,3], 
         [1,6,4], 
         [0,7,5]]

curdown = [[2,8,3], 
         [1,6,4], 
         [0,7,5]]

curleft = [[2, 8, 3],
         [1, 6, 4],
         [0, 7, 5]]

curright = [[2, 8, 3],
         [1, 6, 4],
         [0, 7, 5]]

goal =  [[1,2,3], 
         [8,0,4], 
         [7,6,5]]

def display(state):
  for i in state:
    for j in i:
      print(j, end=" ")
    print()

def getIndex(state, elemant):
  for i in range(3):
    for j in range(3):
      if state[i][j] is elemant:
        yield i
        yield j
        break

def swap(state, i, j, direction):
  temp = state[i][j]
  if direction is 'd' and i is not 0:
    state[i][j] = state[i-1][j]
    state[i-1][j] = temp

  elif direction is 'u' and i is not 2:
    state[i][j] = state[i+1][j]
    state[i+1][j] = temp
  
  elif direction is 'r' and j is not 0:
    state[i][j] = state[i][j-1]
    state[i][j-1] = temp
    
  elif direction is 'l' and j is not 2:
    state[i][j] = state[i][j+1]
    state[i][j+1] = temp    
  return state

def move(state, direction):
  i, j = getIndex(state, 0)
  state = swap(state, i, j, direction)
  #display(state)
  #print(getFScore(state,0))

def getHScore(state):
  HScore = 0
  for i in range(3):
    for j in range(3):
      elemant = state[i][j]
      if elemant is not 0:
       a, b = getIndex(goal,elemant)
       HScore = HScore + abs(i-a) + abs(j-b)
  return HScore

def getGScore(state, prevG):
  GScore = 0
  for i in range(3):
    for j in range(3):
      if goal[i][j] is not state[i][j]:
        GScore += 1
  return prevG + GScore

def getFScore(state, prevF):
  return getHScore(state) + getGScore(state, prevF)

def minn(listCost, up, down, left, right):
  min = 100000
  for i in listCost:
    if i < min:
      min = i

  if min is up:
    return 'u'
  if min is down:
    return 'd'
  if min is left:
    return 'l'
  if min is right:
    return 'r'

close = []
close.append(start)
i=-1
while start is not goal:
  i+=1
  up = down = left = right = 100000
  move(curdown,'d')
  move(curup,'u')
  move(curleft,'l')
  move(curright,'r')

  if curdown not in close:
    down = getFScore(curdown,0)
  if curup not in close:
    up = getFScore(curup,0)
  if curleft not in close:
    left = getFScore(curleft,0)
  if curright not in close:
    right = getFScore(curright, 0)
  listCost = [up, down, left, right]
  s = minn(listCost, up, down, left, right)
  #print(s, end=" ")
  move(start, s)
  close.append([])
  close[i].append(start)
  print()
  close.append(start)


