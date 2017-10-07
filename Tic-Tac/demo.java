class demo
{
  public static int Possible_Wins = 8;
  
  public static int[][] Three_in_a_Row = new int[][] { { 0, 1, 2 }, { 3, 4, 5 }, { 6, 7, 8 }, { 0, 3, 6 }, { 1, 4, 7 }, { 2, 5, 8 }, { 0, 4, 8 }, { 2, 4, 6 } };

  public static int[][] Heuristic_Array = new int[][] {
    {     0,   -10,  -100, -1000 },
    {    10,     0,     0,     0 },
    {   100,     0,     0,     0 },
    {  1000,     0,     0,     0 }
  };

  public static char[] board = new char[9];

  public static int evaluatePosition(char player) {
    int players, others, t = 0, i, j;
    char opponent, piece;
    if(player == 'X')
       opponent = 'O';
    else
      opponent = 'X';

    for (i = 0; i < 8; i++)  {
      players = others = 0;
      for (j = 0; j < 3; j++)  {
        piece = board[Three_in_a_Row[i][j]];
        if (piece == player)
          players++;
        else if (piece == opponent)
          others++;
      }
      t += Heuristic_Array[players][others];
    }  
    return t;
  }

  public static void main(String arg[])
  {
    board[0]='X';
    board[1]='X';
    board[2]='O';
    board[3]='X';
    board[4]='O';
    board[5]='O';
    

    for(int i=0; i<9; i++)
    {
      if(i%3==0)
        System.out.println();
        if(i%2==0)
          System.out.print(" "+evaluatePosition('X'));
        else
          System.out.print(" "+evaluatePosition('O'));
    };
  }
}