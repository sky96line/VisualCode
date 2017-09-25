#include <termios.h>
#include <stdio.h>

static struct termios old, new;

void gotoxy(int x, int y)
{
  printf("%c[%d;%df", 0x1B, y, x);
}

void clrscr(void)
{
  system("clear");
}

void initTermios(int echo)
{
  tcgetattr(0, &old);                 //grab old terminal i/o settings
  new = old;                          //make new settings same as old settings
  new.c_lflag &= ~ICANON;             //disable buffered i/o
  new.c_lflag &= echo ? ECHO : ~ECHO; //set echo mode
  tcsetattr(0, TCSANOW, &new);        //apply terminal io settings
}

void resetTermios(void)
{
  tcsetattr(0, TCSANOW, &old);
}

char getch_(int echo)
{
  char ch;
  initTermios(echo);
  ch = getchar();
  resetTermios();
  return ch;
}

char getch(void)
{
  return getch_(1);
}