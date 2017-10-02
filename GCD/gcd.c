#include <stdio.h>

int gcd(int a, int b)
{
  if(b==0)
    return a;
  return gcd(b, a % b);
}

int main(void)
{
  int result = gcd(20, 10);
  printf("%d", result);
}