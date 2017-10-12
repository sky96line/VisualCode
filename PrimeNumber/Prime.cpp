#include <iostream>
#define SCALE 0.00001

using namespace std;

int pow(int x, int n) {
  if (n == 0)
    return 1;
  int y = pow(x, n / 2);
  if (n % 2 == 0) return y * y;
  else return x * y * y;
}

float SqrRoot(float no) {
  float left, right, mid;
  left = 0;
  right = no;

  while ((right - left) > SCALE) {
    mid = (right + left) / 2;
    if ((mid * mid) == no)
      return mid;
    if ((mid * mid) > no)
      right = mid;
    else
      left = mid;
  }
  return mid;
}

int mul(int num1, int num2) {
  int sum = 0;
  for (int i = num2; i > 0; i--)
    sum += num1;
  return sum;
}

void primes(int num) {
  int total, j, i;
  bool array[num];
  for (i = 0; i < num; i++) {
    array[i] = false;
  }

  for (i = 2; (i * i) < num; i++) {
    if (!array[i]) {
      for (j = 2; j <= num / i; j++) {
        array[(i * j)] = true;
      }
    }
  }

  for (i = 2; i < num; i++)
  {
    if (array[i])
      cout << i << " ";
  }
}

int gcd(int a, int b) {
  return b == 0 ? a : gcd(b, a % b);
}

int fibonacci(int no) {
  if(no==0)
    return 0;
  else if(no==1)
    return 1;
  return fibonacci(no - 1) + fibonacci(no - 2);
}

int main(void) {
  for (int i = 0; i < 10;i++) {
    cout << " "<<fibonacci(i);
  }
  return 0;
}