#include <stdio.h>
#include <stdlib.h>
#include <time.h>


struct poker_t
{
    int num;
    int color;
} poker[52];

char suit;
int number;

void init(struct poker_t *poker)
{
    int index = 0;
    for (int i = 0; i < 4; i++)
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
{
    struct poker_t temp;
    for (int j = 0, i = length; i;)
    {
        j = rand() % i;
        temp = poker[--i];
        poker[i] = poker[j];
        poker[j] = temp;
    }
}

void deal(struct poker_t *poker, int index)
{
    char Poker_str[] = "shdc";
    suit = Poker_str[poker[index].color];
    number = poker[index].num;
}

int index = 0;
int main()
{
    index=0;
    srand(time(NULL));
    init(poker);
    char emit;
    shuffle(poker, 52);
}


// 發下一張牌，0代表沒有牌, 1代表取牌成功
int next()
{
    if (index == 52)
    { // 下次要討論發完該如何處理
        return 0;
    }
    deal(poker, index);
    index++;
    return 1;
}

/*
  輸入A 離開迴圈停止程式
  輸入B 發一張牌 發完52張回傳None停止程式

  input : B   output :(s,10)
  input : B   output :(d,4)
  input : A   output :
*/
