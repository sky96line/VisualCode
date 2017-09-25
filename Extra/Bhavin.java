package demo;

import java.util.Scanner;

public class Bhavin {
  static int no;
  static int[] group;
  static boolean[] chk;
  static Scanner sc = new Scanner(System.in);
  
  static void mamber(int no)
  {
    group = new int[no];
    chk = new boolean[no];
    for(int i=0; i<no; i++)
    {
      group[i] = i+1;
      chk[i] = true;
    }
  }
  
  static void display()
  {
    for(int i=0; i<no; i++)
    {
      System.out.print(" "+group[i]);
    }
    System.out.println();
    for(int i=0; i<no; i++)
    {
      System.out.print(" "+chk[i]);
    }
  }
  
  public static void main(String args[])
  {
    int i,j,diff,count=0,temp=0,e;
    System.out.print("Enter Number of player : ");
    no = sc.nextInt();
    
    System.out.print("Enter Number of diffrence : ");
    diff = sc.nextInt();
    
    mamber(no);
    display();
    
    e=0;
    while(count!=no-1)
    {
      for(i=0; i<no; i++)
      {
        
        if(chk[i])
        {
          temp++;
        }
        if(temp==diff)
        {
          chk[i]=false;
          temp=0;
          count++;
        }
      }
    }
    
    for(i=0; i<no; i++)
    {
      if(chk[i])
        System.out.println(" "+group[i]);
    }
  }
}