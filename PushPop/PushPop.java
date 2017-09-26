class PushPop
{
  static int[] a = new int[10];

  static int len()
  {
    int j=0;
    for(int i=0; i<a.length; i++)
    {
      if(a[i]!=0)
        j++;
    }
    return j;
  }

  static void push(int[] arr, int n)
  {
    for(int i=0; i<arr.length; i++)
    {
      if(arr[i]==0)
      {
        arr[i]=n;
        break;
      }
    }
    a = arr;
  }

  static void pop(int[] arr, int index)
  {
    for(int i=index; i<arr.length-1; i++)
    {
      arr[i]=arr[i+1];
    }
    a = arr;
  }

  static void display(int[] arr)
  {
    for(int i=0; i<arr.length; i++)
    {
      if(arr[i]!=0)
        System.out.println(arr[i]);
    }
  }

  public static void main(String args[])
  {
    push(a,0);
    pop(a);
    display(a);
  }
}