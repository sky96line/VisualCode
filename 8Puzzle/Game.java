
class Node
{
  int[][] bord = new int[3][3];
  int up=0,down=0,left=0,right=0;

  Node(int[][] arr) {
    this.bord = arr;
  }

  int[] indexOf(int no) {
    int[] arr=new int[2];
    boolean flag = false;
    for(int i=0; i<3; i++)  {
      for(int j=0; j<3; j++)  {
        if(bord[i][j]==no) {
          arr[0] = i;
          arr[1] = j;
          flag=true;
          break;
        }
        if(flag)
          break;
      }
    }
    return arr;
  }

  int[] indexOf(int[][] temp, int no) {
    int[] arr=new int[2];
    boolean flag = false;
    for(int i=0; i<3; i++)  {
      for(int j=0; j<3; j++)  {
        if(temp[i][j]==no) {
          arr[0] = i;
          arr[1] = j;
          flag=true;
          break;
        }
        if(flag)
          break;
      }
    }
    return arr;
  }

  int huristic() {
    int prob=0;
    int[] index = new int[2];
    for(int i=0; i<3; i++)
    {
      for(int j=0; j<3; j++)
      {
        index = indexOf(Game.goal[i][j]);
        prob += Math.abs((index[0]-i)+(index[1]-j));
      }
    }
    return prob;
  }
  int huristic(int[][] temp) {
    int prob=0;
    int[] index = new int[2];
    for(int i=0; i<3; i++)
    {
      for(int j=0; j<3; j++)
      {
        index = indexOf(temp, Game.goal[i][j]);
        prob += Math.abs((index[0]-i)+(index[1]-j));
      }
    }
    return prob;
  }

  int[][] swap(int[][] arr, int x, int y, String move )  {
    int temp;
    if(move=="UP")  {
      if(x>0) {
        temp = arr[x][y];
        arr[x][y] = arr[x-1][y];
        arr[x-1][y] = temp;
      }
    } if(move=="DOWN")  {
        if(x<2) {
          temp = arr[x][y];
          arr[x][y] = arr[x+1][y];
          arr[x+1][y] = temp;
        }
    } if(move=="LEFT")  {
        if(y>0) {
          temp = arr[x][y];
          arr[x][y] = arr[x][y-1];
          arr[x][y-1] = temp;
        }
    } if(move=="RIGHT")  {
        if(y<2) {
        temp = arr[x][y];
        arr[x][y] = arr[x][y+1];
        arr[x][y+1] = temp;
      }
    }
    return arr;
  }

  int max(int a, int b, int c, int d)
  {
    if(a>b && a>c && a>d) { return a; }
    else if(b>c && b>d) { return b; }
    else if(c>d) { return c; }
    else { return d; }
  }

  void move(String move)
  {
    int[] index = indexOf(0);
    int temp=0;
    if(move=="UP")
    {
      temp = bord[index[0]][index[1]];
      bord[index[0]][index[1]] = bord[index[0]-1][index[1]];
      bord[index[0]-1][index[1]] = temp;
    }
    if(move=="DOWN")
    {
      temp = bord[index[0]][index[1]];
      bord[index[0]][index[1]] = bord[index[0]+1][index[1]];
      bord[index[0]+1][index[1]] = temp;
    }
    if(move=="LEFT")
    {
      temp = bord[index[0]][index[1]];
      bord[index[0]][index[1]] = bord[index[0]][index[1]-1];
      bord[index[0]][index[1]-1] = temp;
    }
    if(move=="RIGHT")
    {
      temp = bord[index[0]][index[1]];
      bord[index[0]][index[1]] = bord[index[0]][index[1]+1];
      bord[index[0]][index[1]+1] = temp;
    }
  }

  void check()
  {
    int max = max(up, down, left, right);
    if(max==up) { move("UP"); }
    else if(max==down)  { move("DOWN"); }
    else if(max==left)  { move("LEFT"); }
    else  { move("RIGHT"); }
  }

  void moveUp()
  {
    int[][] temp = bord;
    int[] index = indexOf(0);
    up=0;
    if(index[0]!=0)
    {
      temp = swap(temp,index[0],index[1],"UP");
      up = huristic(temp);
    }
  }

  void moveDown()
  {
    int[][] temp = bord;
    int[] index = indexOf(0);
    down=0;
    if(index[0]!=2)
    {
      temp = swap(temp,index[0],index[1],"DOWN");
      down = huristic(temp);
    }
  }

  void moveLeft()
  {
    int[][] temp = bord;
    int[] index = indexOf(0);
    left=0;
    if(index[1]!=0)
    {
      temp = swap(temp,index[0],index[1],"LEFT");
      left = huristic(temp);
    }
  }

  void moveRight()
  {
    int[][] temp = bord;
    int[] index = indexOf(0);
    right=0;
    if(index[1]!=2)
    {
      temp = swap(temp,index[0],index[1],"RIGHT");
      right = huristic(temp);
    }
  }

  void display()  {
    for(int i=0; i<3; i++)  {
      for(int j=0; j<3; j++)  {
        System.out.print(" "+bord[i][j]);
      }
      System.out.println();
    }
  }
}

class Game
{
  public static int[][] goal = new int[][] {{1,2,3},{8,0,4},{7,6,5}};
  static Node n;
  public static void main(String args[])
  {
    int[][] arr = new int[][] {{1,2,3},{4,8,0},{7,6,5}};
    //int[][] arr = new int[][] {{1,2,3},{4,5,6},{7,8,0}};
    n = new Node(arr);
    n.display();
    System.out.println(n.huristic());
  }
}