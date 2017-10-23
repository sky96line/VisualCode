import java.util.*;
class newGame
{
  public static int[][] start = new int[][] {
    {1,2,3}, 
    {4,0,6}, 
    {7,8,5}};
  
  public static int[][] goal = new int[][] {
    {1,2,3}, 
    {4,5,6}, 
    {7,0,8}};

  public static int[][][] closeSet = new int[100][3][3];
  public static Scanner sc = new Scanner(System.in);

  static void display(int[][][] arr) {
    System.out.println();
    for (int k = 0; k < 100; k++) {
      for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
          System.out.print(" " + arr[k][i][j]);
        }
        System.out.println();
      }
    }
  }

  static void display(int[][] arr) {
    System.out.println();
    for(int i=0; i<3; i++)
    {
      for(int j=0; j<3; j++)
      {
  
          System.out.print(" "+arr[i][j]);
      }
      System.out.println();
    }
  }

  static int[] getIndex(int[][] arrGoal, int find) {
    int[] indexes = new int[2];

    for (int i = 0; i < 3; i++) 
    {
      for (int j = 0; j < 3; j++) 
      {
        if(arrGoal[i][j] == find)
        {
          indexes[0] = i;
          indexes[1] = j;
          return indexes;
        }
      }
    }
    return indexes;
  }

  static int getHScore(int[][] arr) {
    int hScore = 0;

    for (int i = 0; i < 3; i++) 
    {
      for (int j = 0; j < 3; j++) 
      {
        if(arr[i][j]!=0)
        {
          int[] index = getIndex(goal,arr[i][j]);
        
          hScore += Math.abs(i- index[0]) + Math.abs(j- index[1]);
        }
      }
    }
    return hScore;
  }

  static int getGScore(int[][] arr) {
    int gScore = 0;

    for(int i=0; i<3; i++)
    {
      for(int j=0; j<3; j++)
      {
        if(arr[i][j] != goal[i][j] && arr[i][j] != 0)
        {
          gScore++;
        }
      }
    }
    return gScore;
  }

  static int finalScore(int[][] arr) {
    return getGScore(arr) + getHScore(arr);
  }

  static int[][] move(int[][] arr, char direction) {
    int[][] newState = arr;
    int[] index = getIndex(arr, 0);
    int temp = 0;

    if(direction == 'u' && index[0] != 2)
    {
      newState[index[0]][index[1]] = newState[index[0]+1][index[1]];
      newState[index[0]+1][index[1]] = 0;
    }
    if(direction == 'd' && index[0] != 0)
    {
      newState[index[0]][index[1]] = newState[index[0]-1][index[1]];
      newState[index[0]-1][index[1]] = 0;
    }
    if (direction == 'l' && index[1] != 2) 
    {
      newState[index[0]][index[1]] = newState[index[0]][index[1] + 1];
      newState[index[0]][index[1] + 1] = 0;
    }
    if(direction == 'r' && index[1] != 0)
    {
      newState[index[0]][index[1]] = newState[index[0]][index[1] - 1];
      newState[index[0]][index[1] - 1] = 0;
    }

    return newState;
  }

  static boolean isVisited(int[][] arr)
  {
    for(int k=0; k<100; k++)
    {
      int c = 0;
      for(int i=0; i<3; i++)
      {
        for(int j=0; j<3; j++)
        {
          if(closeSet[k][i][j] == arr[i][j])
            c++;
        }
      }
      if(c==9)
      {
        return true;
      }  
    }
    return false;
  }

  public static void main(String args[])
  {
    
    int[][] state = start;
    int[][] stateUp = start;
    int[][] stateDown = start;
    int[][] stateLeft = start;
    int[][] stateRight = start;
    
    display(state);
    stateUp = move(stateUp, 'u');
    display(stateUp);
    stateDown = move(stateDown, 'd');
    display(stateDown);
    stateLeft = move(stateLeft, 'l');
    display(stateLeft);
    stateRight = move(stateRight, 'r');
      
    
    
    
    
    display(stateRight);
    
  }
}