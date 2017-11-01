#include <iostream>
#define SCALE 0.00001

using namespace std;

void swapChar(char *a, char *b) {
  char temp;
  temp = *a;
  *a = *b;
  *b = temp;
}

//Recursion
int pow(int x, int n) {
  if (n == 0)
    return 1;
  int y = pow(x, n / 2);
  if (n % 2 == 0) return y * y;
  else return x * y * y;
}

//D&C
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

//Recursion
int gcd(int a, int b) {
  return b == 0 ? a : gcd(b, a % b);
}

//Recursion
int fibonacci(int no) {
  if(no==0 || no==1)
    return no;
  return fibonacci(no - 2) + fibonacci(no - 1);
}

void grayCodeHelper(int bytes, string pre)  {
  if(bytes==0)
    cout << pre << endl;
  else  {
    grayCodeHelper(bytes - 1, pre + "0");
    grayCodeHelper(bytes - 1, pre + "1");
  }
}

//Recursion
void grayCode(int bytes)  {
  grayCodeHelper(bytes, "");
}

//Back-Tracking
void permute(char* str, int l, int r) {
  int i;
  if (l == r)
    cout << str << endl;
  else  {
    for (i = l; i <= r; i++) {
      swapChar((str + l), (str + i));
      permute(str, l + 1, r);
      swapChar((str + l), (str + i));
    }
  }
}

int main(void)
{
  char a[] = "abcd";
  permute(a, 0, 3);
  return 0;
}