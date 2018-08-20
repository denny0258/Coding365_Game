cdef extern from '../winner.c':
    # 設定玩家數量
    # count: 玩家數量
    cpdef void set_player_count(int count)

    # 設定玩家牌數量與生死狀態 (死代表超過21)
    # pid: 玩家編號
    # count: 玩家持有牌數量
    # life: 0:死 1:生
    cpdef void set_card_count(int pid, int count, int life)

    # 設定玩家牌面
    # pid: 玩家編號，0~19
    # cid: 牌編號, 0~19: 第 n 張牌
    # 
    # 牌面:
    # suit: 1 黑桃 2 紅心 3 菱形 4 梅花
    # number: 1~13
    cpdef void set_card(int pid, int cid, int suit, int number)

    # 是否為贏家
    # pid: 玩家編號: 0~19
    # return: 0:輸 1:贏家
    cpdef int get_is_winner(int pid)