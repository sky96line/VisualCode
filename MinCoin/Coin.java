import java.util.Arrays;

class coin
{
 
  static int minCoins(int coins[], int m, int V)
  {
  
    int[] table = new int[V+1];
    Arrays.fill(table, Integer.MAX_VALUE);
    table[0]=0;
    
    for(int i=1; i<=V; i++)
    {
      for(int j=0; j<m; j++)
      {
        if(coins[j]<=i)
        {
          int sub = table[i-coins[j]];
          if((sub+1) < table[i])
            table[i] = sub+1;
        }
      }
    }
    return table[V];
  }
  
  public static void main(String args[])
  {
    int coins[] =  {6,4,1};
    int m = coins.length;
    int V = 8;
    System.out.println("Minimum coins required is "+ minCoins(coins, m, V) );
  }
}