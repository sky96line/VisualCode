package demo;

import java.util.*;

class Edge
{
  public int[] node = new int[2];
  public int dist;
  
  Edge(int i, int j, int dist)
  {
    this.node[0] = i;
    this.node[1] = j;
    this.dist = dist;
  }
  
  int getNode0()
  {
    return node[0];
  }
  
  int getNode1()
  {
    return node[1];
  }
  
  int[] getNodes()
  {
    return node;
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

class Kruskal
{
  public static int size;
  public static int[][] matrix;
  public static Edge[] e;
  public static int numEdge=0;
  public static Scanner sc = new Scanner(System.in);
  
  static boolean chack(int x, int y, int[] arr)
  {
    boolean flag1, flag2;
    for(int i=0; i<arr.length; i++)
    {
      if(x==arr[i])
      {
        flag1 = true;
        break;
      }
    }
    for(int i=0; i<arr.length; i++)
    {
      if(y==arr[i])
      {
        flag2 = true;
        break;
      }
    }
    return (flag1||flag2);
  }

  static int[] done()
  {
    boolean flag;
    int c=0,total=0;
    int[] closeSet = new int[size*2];
    for(int i=0; i<size; i++) {
      int min = 0;
      for(int j=0; j<numEdge; j++)  {
        if(e[min].getDist()>e[j].getDist() && e[j].getDist()!=0)
          min = j;
      }
      
      flag = ckack(e[min].getNode0(), e[min].getNode0(), closeSet);
      
      System.out.println(e[min].getDist());
      if(flag){}
      else  {
        closeSet[c++]=e[min].getNode0();
        closeSet[c++]=e[min].getNode1();
        total += e[min].getDist();
        e[min].setDist(10000);
      }
    }
    System.out.println(total);
    return closeSet;
  }
  
  static void fill()
  {
    for(int i=0; i<size; i++)
    {
      matrix[i][i]=0;
      for(int j=i+1; j<size; j++)
      {
        System.out.print(i+" to "+j+" : ");
        int dist = sc.nextInt();
        matrix[i][j] = dist;
        matrix[j][i] = dist;
        if(dist>0)
        {
          e[numEdge++] = new Edge(i,j,dist);       
        }
      }
    }
  }

  static void display()
  {
    for(int i=0; i<size; i++)
    {
      for(int j=0; j<size; j++)
      {
        System.out.print(" "+matrix[i][j]);
      }
      System.out.println();
    }
  }
  
  static void display(int[] m)
  {
    for(int i=0; i<m.length; i++)
    {
      if(m[i]!=0)
        System.out.print(" "+m[i]);
    }
  }
  
  static void displayEdge()
  {
    for(int i=0; i<numEdge; i++)
    {
      int[] arr = e[i].getNodes();
      System.out.println(arr[0] + " to " + arr[1] + " : " + e[i].getDist());
    }
  }

  public static void main(String args[])
  {
    System.out.print("How many node are there : ");
    size = sc.nextInt();
    e = new Edge[14];
    matrix = new int[size][size];
    fill();
    int[] arr = done();
    //display(arr);
  }
}