count_pla = 1
dict1={}

#輸入電腦人數，玩家人數
class Player_Control:
    def __init__(self):
        self.setname()
        # self.life = True
        # self.cards = []
#第一次加入時    
    def setname(self):
        global count_pla
        print('請輸入玩家名稱')#what is your name?
        self.username = 'Player'+str(count_pla)
        self.username = input()

    def join(self):
        print('是否加入此局？')'join? y/n'
        print('加入請輸入y，拒絕加入請輸入n')
        if input() == 'y':
            return True
        return False

    #def event():
        
#每局都要問    
    def take(self, my_Cards ):#my_Cards從外面輸入，發牌系統還是等抹？
        print('your card:', my_Cards)
        print('want more? y/n')
        if input() == 'y':
            return True
        return False
    
#爆炸的假設
    def a(income):#呼叫偵測是否爆炸



count_com = 1

class Computerr_Control(Playerr_Control):
    
    def setname(self):
        global count_com
        self.username='Computer'+str(count_com)
        count_com+=1

    def join(self):
        return True






{
    "username": String # 玩家名稱
    "life": True|False,
    "cards": [ Card, ...],
    {"username": String}:{"life": True|False,"cards": [ Card, ...]}
    # 是否下注
    join() -> True|False # True: 下注
    # 是否拿牌
    take( my_cards ) -> True|False # True: 拿
    # 遊戲事件
    game_event( event )
}

my_cards: [ Card, ... ]  # 現有牌面 

event: {
    "player": String     # 玩家名稱
    "take":   True|False # 是否拿牌 True: 拿
    "life":   True|False # 是否死亡 True: 生存
}





def Test(Test_Data):
    if Test_Data.get("Hello", None) == True:
        return {"World": True}