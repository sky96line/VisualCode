#include <stdio.h>

void display(int table[], int target)
{
  int i = 0;
  for (i = 0; i <= target;i++)
    printf(" %d", table[i]);
}

int MinRod(int target, int len[], int profit[])
{
  int i = 0, j = 0;
  int size = sizeof(len);
  int table[target + 1];
  for (i = 0; i <= target; i++)
  {
    table[i] = i;
  }
  for (i = 1; i <= target;i++)
  {
    for (j = 0; j < size;j++)
    {
      if(len[j]<=i)
      {
        int sub = table[i - len[j]];
        if(sub + profit[j] > table[i])
          table[i] = sub + profit[j];
      }
    }
    display(table, target);
    printf("\n");
  }
  return table[target];
}

int main(void)
{
  int len[] = {1, 2, 4};
  int profit[] = {1, 5, 8};
  int target = 5;
  int result = MinRod(target, len, profit);
  printf("%d", result);
  return 0;
}