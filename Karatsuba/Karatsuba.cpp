#include <cstdlib>
#include <iostream>
#include <math.h>
#define base 10

using namespace std;


int front(int x)
{
  return x / base;
}

int back(int y)
{
  return y % base;
}

int karatsuba(int x, int y)
{
  if(x<base || y<base)
    return x * y;

  int a = front(x);
  int b = back(x);
  int c = front(y);
  int d = back(y);

  int z0 = karatsuba(b, d);
  int z2 = karatsuba(a, c);
  int z1 = karatsuba((a + b), (c + d)) - z0 - z2;

  return (z2 * pow(base, 2)) + (z1 * base) + z0;
}

int main(void)
{
  int result=0, z0, z1, z2, x, y, a, b, c, d;

  cout << "Enter first number : ";
  cin >> x;
  cout << "Enter second number : ";
  cin >> y;

  result = karatsuba(x, y);
  cout
      << endl
      << "Result is : " << result;

  return 0;
}