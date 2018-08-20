#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct poker_t {
   int num ;
   int color ;
}poker[52];
void init(struct poker_t *poker){
    int index =0;
    for(int i=0 ;i<4 ; i++){
        for(int j=1;j<=13;j++){
          poker[index].color = i ;
          poker[index].num = j ;
          index ++;
        }
    }
}

void shuffle(struct poker_t *poker, int length){

    struct poker_t temp ;
    for(int j=0, i=length; i;){
        j = rand()%i;
        temp = poker[--i];
        poker[i] = poker[j];
        poker[j] = temp;
    }
}

void deal(struct poker_t *poker,int index){
     char Poker_str[] = "shdc";
     printf("(%c,%d)\n",Poker_str[poker[index].color],poker[index].num);
}

int main(){
  srand(time(NULL));
  int index =0;
  init(poker);
  char emit ;
  shuffle(poker,52);
  while(1){
     scanf("%c",&emit);

     if(emit == 'A') break ;
     if(emit == 'B'){
        if(index == 52){  // 下次要討論發完該如何處理
          printf("None\n");
          break;
        }
        deal(poker,index);
        index ++;
     }
  }

  return 0;
}
/*
  輸入A 離開迴圈停止程式
  輸入B 發一張牌 發完52張回傳None停止程式

  input : B   output :(s,10)
  input : B   output :(d,4)
  input : A   output :
*/
