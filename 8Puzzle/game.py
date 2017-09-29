from __future__ import print_function
class bord:
  #state = [[0,0,0],[0,0,0],[0,0,0]]
  
  def __init__(self, list):
    k=1
    for i in bord.state:
      for j in i:
        print(bord.state[j])

  def display(self):
    print("==========")
    print( "|", bord.state[0][0], "|" ,bord.state[0][1], "|", bord.state[0][2] ,"|" )
    print( "|", bord.state[1][0], "|" ,bord.state[1][1], "|", bord.state[1][2] ,"|" )
    print( "|", bord.state[2][0], "|" ,bord.state[2][1], "|", bord.state[2][2] ,"|" )
    print("==========")

list = [1,2,3,4,5,6,7,8,9]
b = bord(list)
#b.display()
