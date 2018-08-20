#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct poker_t
{
  int num;
  int color;
} poker[52];

int suit;
int number;

void init(struct poker_t *poker)
{ //初始化樸克牌陣列
  int index = 0;
  for (int i = 1; i <= 4; i++)
  {
    for (int j = 1; j <= 13; j++)
    {
      poker[index].color = i;
      poker[index].num = j;
      index++;
    }
  }
}
void shuffle(struct poker_t *poker, int length)
{ //隨機洗牌
  srand(time(NULL));
  struct poker_t temp;
  for (int j = 0, i = length; i;)
  {
    j = rand() % i;
    temp = poker[--i];
    poker[i] = poker[j];
    poker[j] = temp;
  }
}
int index = 0;
void do_shuffle()
{ //執行洗牌功能
  index = 0;
  shuffle(poker, 52);
}
int do_next()
{
  if (index == 52)
    return 0;
  suit = poker[index].color;
  number = poker[index].num;
  index++;
  return 1;
}
void do_init()
{
  init(poker);
}
int main()
{
  return 0;
}
/*
  do_init()  執行初始化 
  do_shuffle() 執行洗牌
  do_next()  執行取牌
*/
