import java.util.*;

class Edge
{
  public int node1;
  public int node2;
  public int dist;
  
  Edge(int i, int j, int dist)
  {
    this.node1 = i;
    this.node2 = j;
    this.dist = dist;
  }
  
  int getNode1()
  {
    return node1;
  }
  
  int getNode2()
  {
    return node2;
  }
  
  int getDist()
  {
    return dist;
  }
  
  void setDist(int n)
  {
    this.dist = n;
  }
}

class newKruskal
{
  //public static int[] value = new int[] {4,2,0,0,0,4,0,0,0,3,2,4,0,3,3};
  //public static int valueI=0;
  public static int size;
  public static int[][] matrix;
  public static int[] closeSet;
  public static Edge[] e;
  public static int c=0;
  public static int numEdge=0;
  public static Scanner sc = new Scanner(System.in);

  public static void fill()
  {
    for(int i=0; i<size; i++)
    {
      for(int j=i+1; j<size; j++)
      {
        int dist = value[valueI++];
        System.out.println(i+" to "+j+" : "+dist);
        //int dist = sc.nextInt();
        if(dist>0)
        {
          e[numEdge++] = new Edge(i,j,dist);       
        }
        else{dist = 10000;}
        matrix[i][j] = dist;
        matrix[j][i] = dist;
      }
    }
  }

  static void sort()
  {
    int min=0;
    for(int i=0; i<numEdge-1; i++)
    {
      min = i;
      for(int j=i+1; j<numEdge; j++)
      {
        if(e[min].getDist()>e[j].getDist())
          min = j;
      }
      Edge temp = e[min];
      e[min] = e[i];
      e[i] = temp;
    }
  }

  static void display()
  {
    for(int i=0; i<numEdge; i++)
    {
      Edge a = e[i];
      System.out.println(a.node1+" "+a.node2+" "+a.dist);
    }
  }

  static boolean check(Edge e)
  {
    boolean flag1=false;
    boolean flag2=false;

    for(int i=0; i<c; i++)
    {
      if(closeSet[i]==e.getNode1())
      {
        flag1 = true;
        break;
      }  
    }
    if(!flag1)
        closeSet[c++]=e.getNode1();
    
    for(int i=0; i<c; i++)
    {
      if(closeSet[i]==e.getNode2())
      {
        flag2 = true;
        break;
      }  
    }

    if(!flag2)
      closeSet[c++]=e.getNode2();

    if(flag1)
    {
      if(flag2)
        return false;
    }
      return true;
  }

  static void done()
  {
    int z=0;
    int total=0;
    System.out.println();
    for(int i=0; i<numEdge || z<size-1; i++)
    {
      boolean flag = check(e[i]);
      if(flag)
      {
        z++;
        System.out.print(" "+e[i].getDist());
        total += e[i].getDist();
      }
    }
    System.out.println();
    System.out.println("Total is : "+total);
  }
  static void displayClose()
  {
    for(int i=0; i<c; i++)
    {
      System.out.print(" "+closeSet[i]);
    }
  }
  public static void main(String args[])
  {
    System.out.print("How many node are there : ");
    size = sc.nextInt();
    System.out.print("How many edge are there : ");
    int s = sc.nextInt();
    closeSet = new int[size];
    matrix = new int[size][size];
    e = new Edge[s];
    closeSet = new int[size];
    fill();
    sort();
    //display();
    done();
  }
}