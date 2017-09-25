import java.util.Arrays;
import java.util.Scanner;

class Node
{
  public String name;
  public int[] assosiate;
  public int[] dist;
  
  Node(String name)
  {
    this.name = name;
    assosiate = new int[Graph.num];
    dist = new int[Graph.num];
    Arrays.fill(dist, -1);
    Arrays.fill(assosiate, 0);
  }
  
  boolean isAssosiated(int node)
  {
    for(int i=0; i<assosiate.length; i++)
    {
      if(assosiate[i] == node)
        return true;
    }
    return false;
  }
  
  void setParameter(int ass, int dist)
  {
    assosiate[ass-1] = ass;
    this.dist[ass-1] = dist;
  }
  
  void display()
  {
    System.out.println("Node : "+name);
    for(int i=0; i < dist.length; i++)
    {
      System.out.println("    "+assosiate[i]+" : "+dist[i]);
    }
    System.out.println();
  }
}

public class GraphViz
{
  static Scanner sc = new Scanner(System.in);
  static Node[] node = new Node[10000];
  public static int num=0;
  
  public static void main(String args[])
  {
    System.out.print("Number of Nodes : ");
    num = sc.nextInt();
    
    for(int i=0; i<num; i++)
    {
      System.out.print("Number of Nodes assosiate with node "+ (i+1) +" : ");
      int no = sc.nextInt();
      
      node[i] = new Node(String.valueOf((i+1)));
      
      for(int j=0; j<no; j++)
      {
        System.out.print("Node assosiate with "+ (i+1) +" : ");
        int ass = sc.nextInt();
        System.out.print("Distance to node "+ (i+1) +" : ");
        int dist = sc.nextInt();
        node[i].setParameter(ass-1, dist);
      }
    }
    
    //int[][] adj = matrix();
    
    for(int i=0; i<num; i++)
    {
      int[] d = node[i].dist;
      for(int j=0; j<num; j++)
      {
        System.out.print(" "+d[j]);
      }
      System.out.println();
    }
    
    /*
    for(int i=0; i<num; i++)
    {
      node[i].display();
    }
    */
    
  }
}