from __future__ import print_function


class game:
  bord = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  player = True
  player1 = None
  player2 = None

  def __init__(self, player1, player2):
    game.player1 = player1
    game.player2 = player2

  def display(self):
    for i in range(3):
      for j in range(3):
        print(game.bord[i][j], end=" ")
      print()

  def mark(self):
    m = int(input("Enter position : "))
    for i in range(3):
      for j in range(3):
        if game.bord[i][j] == m:
          if game.player:
            game.bord[i][j] = 'X'
            game.player = False
          else:
            game.bord[i][j] = 'O'
            game.player = True
          self.display()

  def isWin(self):
    if (game.bord[0][0] == game.bord[0][1] == game.bord[0][2]):
      return True

    elif (game.bord[1][0] == game.bord[1][1] == game.bord[1][2]):
      return True

    elif (game.bord[2][0] == game.bord[2][1] == game.bord[2][2]):
      return True

    elif (game.bord[0][0] == game.bord[1][0] == game.bord[2][0]):
      return True

    elif (game.bord[0][1] == game.bord[1][1] == game.bord[2][1]):
      return True

    elif (game.bord[0][2] == game.bord[1][2] == game.bord[2][2]):
      return True

    elif (game.bord[0][0] == game.bord[1][1] == game.bord[2][2]):
      return True

    elif (game.bord[0][2] == game.bord[1][1] == game.bord[2][0]):
      return True

    else:
      return False


x = raw_input("Player 1 : ")
y = raw_input("player 2 : ")
a = game(x, y)
while i in range(9):
  a.mark()
  if a.isWin():
    if game.player:
      print("{} win".format(a.player2))
    else:
      print("{} win".format(a.player1))
    break
