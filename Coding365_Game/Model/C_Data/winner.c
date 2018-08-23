#include<stdio.h>
#include<limits.h>

int play_num=0; //玩家數量
int get =0 ;
int max_point =0 ;
struct card_t{
   int suit ;
   int number ;
};
struct Playinfo_t{
    int life ; //玩家是否生存
    int winner ;//是否是贏家
    int sum ; //玩家手牌點數和
    int count ; //玩家持有牌數
    struct card_t card[19] ;
}play_info[19];

void set_player_count(int count){
     play_num = count  ;
}

void set_card_count(int pid, int count, int life){
     play_info[pid].count = count ;
     play_info[pid].winner = 0 ;
     play_info[pid].life = life ;
}

void set_card(int pid, int cid, int suit, int number){
     play_info[pid].card[cid].suit = suit ;
     play_info[pid].card[cid].number = number ;
}

void sum(int pid , int count){
    play_info[pid].sum =0;

     for(int i=0 ;i<count;i++){
       if(play_info[pid].card[i].number >= 10)
          play_info[pid].sum += 10;   
       else 
          play_info[pid].sum += play_info[pid].card[i].number ; 
     }
}
void sum_total(){
    for(int i=0;i<play_num;i++){
      if(play_info[i].life == 1)
         sum(i,play_info[i].count);
      else continue ;
    }
}

void find_max(){
    sum_total();
    max_point =INT_MIN ;
    for(int i=0 ; i<play_num ; i++)
       if(play_info[i].sum > max_point)
          max_point = play_info[i].sum ;
}

void winner(){
     find_max();
     for(int i =0;i<play_num ;i++)
        if(play_info[i].sum == max_point)
            play_info[i].winner = 1 ;
}

int get_is_winner(int pid){
    if(get == 0){ 
       winner();
       get ++ ;
    }
    if(play_info[pid].winner == 1)
         return 1 ;
    else 
         return 0 ;
}
void main(){
}
/*
// 設定玩家數量
// count: 玩家數量
void set_player_count(int count)

// 設定玩家牌數量與生死狀態 (死代表超過21)
// pid: 玩家編號
// count: 玩家持有牌數量
// life: 0:死 1:生
void set_card_count(int pid, int count, int life)

// 設定玩家牌面
// pid: 玩家編號，0~19
// cid: 牌編號, 0~19: 第 n 張牌
// 
// 牌面:
// suit: 1 黑桃 2 紅心 3 菱形 4 梅花
// number: 1~13
void set_card(int pid, int cid, int suit, int number)

// 是否為贏家
// pid: 玩家編號: 0~19
// return: 0:輸 1:贏家
int get_is_winner(int pid)
*/