import java.util.*;

class huristic
{
  public static int[][] prob = new int[][] {{3,2,3},{2,4,2},{3,2,3}};
  public static char[][] board = new char[][] {{'?','?','?'},{'?','?','?'},{'?','?','?'}};

  public static void display(char arr[][])
  {
    System.out.println();
    for(int i=0; i<3; i++)  {
      for(int j=0; j<3; j++)  {
        System.out.print(" "+arr[i][j]);
      } System.out.println();
    }
  }

  public static void display(int arr[][])
  {
    System.out.println();
    for(int i=0; i<3; i++)  {
      for(int j=0; j<3; j++)  {
        System.out.print(" "+arr[i][j]);
      } System.out.println();
    }
  }

  public static void updateScore(int x, int y, boolean player)
  {
    int score = prob[x][y];
    int s=1;

    if(player)
    {
      for(int i=0; i<3; i++)
      {
        if(board[x][i]=='X') s++;
      }
      for(int i=0; i<3; i++)
      {
        prob[x][i] += score * s;
      }
      s=1;
      for(int i=0; i<3; i++)
      {
        if(board[i][y]=='X') s++;
      }
      for(int i=0; i<3; i++)
      {
        prob[i][y] += score * s;
      }
      if(x==1 && y==1)
      {
        s=0;
        for(int i=0; i<3; i++)
        {
          if(board[i][i]=='X') s++;
        }
        if(board[2][0] == 'X') s++;
        if(board[0][2] == 'X') s++;

        for(int i=0; i<3; i++)
          prob[i][i] += score * s;
        prob[2][0] += score * s;
        prob[0][2] += score * s ;
      }
      else if(x==0 && y==0)
      {
        s=0;
        for(int i=0; i<3; i++)
        {if(board[i][i]=='X') s++;}
        for(int i=0; i<3; i++)
          prob[i][i] += score * s;
      }
      else if(x==2 && y==2)
      {
        s=0;
        for(int i=0; i<3; i++)
        {if(board[i][i]=='X') s++;}
        for(int i=0; i<3; i++)
          prob[i][i] += score;
      }
      else if(x==0 && y==2)
      {
        s=0;
        if(board[0][2] == 'X') s++;
        if(board[1][1] == 'X') s++;
        if(board[2][0] == 'X') s++;

        prob[0][2] += score * s;
        prob[1][1] += score * s;
        prob[2][0] += score * s;
      }
      else
      {
        s=0;
        if(board[0][2] == 'X') s++;
        if(board[1][1] == 'X') s++;
        if(board[2][0] == 'X') s++;

        prob[0][2] += score;
        prob[1][1] += score;
        prob[2][0] += score;
      }
    }
    else
    {
      for(int i=0; i<3; i++)
      {
        prob[x][i] -= score;
      }
      for(int i=0; i<3; i++)
      {
        prob[i][y] -= score;
      }
      if(x==1 && y==1)
      {
        for(int i=0; i<3; i++)
          prob[i][i] -= score;
        prob[2][0] -= score;
        prob[0][2] -= score;
      }
      else if(x==0 && y==0)
      {
        for(int i=0; i<3; i++)
          prob[i][i] -= score;
      }
      else if(x==2 && y==2)
      {
        for(int i=0; i<3; i++)
          prob[i][i] -= score;
      }
      else if(x==0 && y==2)
      {
        prob[0][2] -= score;
        prob[1][1] -= score;
        prob[2][0] -= score;
      }
      else
      {
        prob[0][2] -= score;
        prob[1][1] -= score;
        prob[2][0] -= score;
      }
      player = !player;
    //display(prob);
    }
  }

  public static void fill(int x, int y, boolean player)
  {
    if(player)
    {
      board[x][y] = 'X';
    }
    else
    {
      board[x][y] = 'O';
    }
    display(prob);
    display(board);
    updateScore(x,y, player);
  }

  public static boolean isEmpty(int x, int y)
  {
    if(board[x][y]=='?')
      return true;
    return false;
  }

  public static void bestFill(boolean player)
  {
    int max=Integer.MIN_VALUE,x=0,y=0;
    
      for(int i=0; i<3; i++)
      {
        for(int j=0; j<3; j++)
        {
          if(isEmpty(i,j))
          {
            if(prob[i][j]>max)
            {
              x = i;
              y = j;
              max = prob[i][j];
            }
          }
        }
      }
    fill(x,y,player);
  }

  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    boolean player = true;
    
    for(int i=0; i<9; i++)
    {
      bestFill(player);
      player = !player;
    }
  }
}