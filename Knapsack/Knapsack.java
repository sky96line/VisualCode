public class Knapsack {
  static final int ITEM = 3;
  static float[] price = new float[ITEM];
  static float[] weight = new float[ITEM];
  static float[] avg = new float[ITEM];
  static float total = 20;
  static float w = 0;
  
  void fill()
  {
    price[0] = 25;
    weight[0] = 18;
    
    price[1] = 24;
    weight[1] = 15;
    
    price[2] = 15;
    weight[2] = 10;
  }
  
  void average()
  {
    for(int i=0; i<ITEM; i++)
    {
      avg[i] = price[i]/weight[i];
    }
  }
  
  int maxIndex(float arr[])
  {
    int index=0;
    for(int i=0; i<arr.length; i++)
    {
      if(arr[index]<arr[i])
        index = i;
    }
    return index;
  }
  
  public static void main(String args[])
  {
    int index;
    float get=0;
    Knapsack g = new Knapsack();
    g.fill();
    g.average();
    
    while(true)
    {
      if(w==total)
        break;
      index = g.maxIndex(avg);
      if(weight[index]<(total-w))
      {
        get = get + (avg[index]*weight[index]);
        w = w + weight[index];
        avg[index] = 0;
      }
      else
      {
        get = get + (avg[index]*(total-w));
        w = w + (total-w);
      }
    }
    System.out.println("  "+get);
  }
}