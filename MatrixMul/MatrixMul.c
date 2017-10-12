#include <stdio.h>

int matrixMul(int arr[], int i, int j) {
  
  if(i==j)
    return 0;
  int k;
  int min = 100000;
  int ans;
  for (k = i; k < j;k++) {
    ans = matrixMul(arr, i, k) + matrixMul(arr, k + 1, j) + arr[i - 1] * arr[k] * arr[j];
    if (min > ans) {
      min = ans;
    }
  }
  return min;
}

int MatrixChainOrder(int p[], int n)
{
  int m[n][n];

  int i, j, k, L, q;

  for (i = 1; i < n; i++)
    m[i][i] = 0;

  for (L = 2; L < n; L++)
  {
    for (i = 1; i < n - L + 1; i++)
    {
      j = i + L - 1;
      m[i][j] = 1000000;
      for (k = i; k < j; k++)
      {
        q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j];
        if (q < m[i][j])
          m[i][j] = q;
      }
    }
  }

  return m[1][n - 1];
}

int main(void) {
  int p[] = {1, 2, 3, 4, 3};
  printf("%d", MatrixChainOrder(p, 5));
}