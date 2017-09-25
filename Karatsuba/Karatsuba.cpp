#include <cstdlib>
#include <iostream>
#include <math.h>
#define base 1000

using namespace std;

int front(int x)
{
  return x / base;
}

int back(int y)
{
  return y % base;
}

int smallMul(int x, int y)
{
  return x * y;
}

int action(int x, int y, int z)
{
  return (x * pow(base, 2)) + (y * base) + z;
}

int main(void)
{
  int result, z0, z1, z2, x, y, a, b, c, d;

  cout << "Enter first number : ";
  cin >> x;
  cout << "Enter second number : ";
  cin >> y;

  a = front(x);
  b = back(x);
  c = front(y);
  d = back(y);

  z0 = smallMul(b, d);
  z2 = smallMul(a, c);
  z1 = smallMul((a + b), (c + d)) - z0 - z2;

  result = action(z2, z1, z0);

  cout << endl
       << "Result is : " << result;

  return 0;
}