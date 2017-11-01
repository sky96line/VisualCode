#include <stdio.h>

int max(int a, int b) {
  return a > b ? a : b;
}

void disp(int *arr, int m, int n)  {
  int i, j;
  for (i = 0; i <= m; i++) {
    for (j = 0; j <= n; j++)  {
      printf("%d ", *((arr+i*n) + j));
    }
    printf("\n");
  }
}

int lcs(char *X, char *Y, int m, int n)
{
  int L[m + 1][n + 1];
  int i, j;

  for (i = 0; i <= m; i++)
  {
    for (j = 0; j <= n; j++)
    {
      if (i == 0 || j == 0)
        L[i][j] = 0;

      else if (X[i - 1] == Y[j - 1])
        L[i][j] = L[i - 1][j - 1] + 1;

      else
        L[i][j] = max(L[i - 1][j], L[i][j - 1]);
    }
  }
  //disp((int *)L, m, n);
  return L[m][n]-1;
}

int main(void) {
  char x[] = "acc";
  char y[] = "acc";
  int m = sizeof(x) / sizeof(x[1]);
  int n = sizeof(y) / sizeof(y[1]);

  printf("%d", lcs(x, y, m, n));
}