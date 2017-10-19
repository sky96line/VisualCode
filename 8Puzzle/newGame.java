
class newGame
{
  public static int[][] start = new int[][] {{2,8,3},{1,6,4},{0,7,5}};
  public static int[][] goal = new int[][] {{1,2,3},{8,0,4},{7,6,5}};
  public static int[][] currentUp = new int[][] { { 2, 8, 3 }, { 1, 6, 4 }, { 0, 7, 5 } };
  public static int[][] currentDown = new int[][] { { 2, 8, 3 }, { 1, 6, 4 }, { 0, 7, 5 } };
  public static int[][] currentLeft = new int[][] { { 2, 8, 3 }, { 1, 6, 4 }, { 0, 7, 5 } };
  public static int[][] currentRight = new int[][] { { 2, 8, 3 }, { 1, 6, 4 }, { 0, 7, 5 } };
  
  static void display(int[][] state)
  {
    for(int i=0; i<3; i++) {
      for(int j=0; j<3; j++) {
        System.out.print(" "+state[i][j]);
      }
      System.out.println();
    }
  }

  static int[] getIndex(int[][] state, int elemant) {
    int[] index = new int[] {0,0};
    for(int i=0; i<3; i++) {
      for(int j=0; j<3; j++) {
        if(state[i][j] == elemant) {
          index = new int[] {i,j};
          return index;
        }
      }
    }
    return index;
  }

  static int[][] swap(int[][] state, int i, int j, char direction) {
    int temp = state[i][j];
    if(direction == 'd' && i!=0) {
      state[i][j] = state[i-1][j];
      state[i-1][j] = temp;
    }
    else if(direction == 'u' && i!=2) {
      state[i][j] = state[i+1][j];
      state[i+1][j] = temp;
    }
    else if(direction == 'r' && j!=0) {
      state[i][j] = state[i][j-1];
      state[i][j-1] = temp;
    }
    else if(direction == 'l' && j!=2) {
      state[i][j] = state[i][j+1];
      state[i][j+1] = temp;
    }
    return state;
  }

  static void move(int[][] statee, char direction) {
    int[][] state = statee;
    int[] index = getIndex(state, 0);
    state = swap(state, index[0], index[1], direction);
    //display(state);
    //System.out.println(getFScore(state,0));
  }

  static int getHScore(int[][] state) {
    int elemant,HScore = 0;
    int[] index;
    for(int i=0; i<3; i++) {
      for(int j=0; j<3; j++) {
        elemant = state[i][j];
        if(elemant != 0) {
          index = getIndex(goal,elemant);
          HScore += Math.abs(i-index[0]) + Math.abs(j-index[1]);
        }
      }
    }
    return HScore;
  }

  static int getGScore(int[][] state,int prevG) {
    int GScore = 0;
    for(int i=0; i<3; i++) {
      for(int j=0; j<3; j++) {
        if(goal[i][j] != state[i][j])
          GScore += 1;
      }
    }
    return prevG + GScore;
  }
  
  static int getFScore(int[][] state, int prevF) {
    return getHScore(state) + getGScore(state, prevF);
  }

  public static void main(String args[])
  {
    close
    while(start == goal)
    {
      int up = 10000, down = 10000, left = 10000, right = 10000;
      move(currentUp,'u');
      move(currentDown,'d');
      move(currentLeft,'l');
      move(currentRight,'r');

    }
  }
}