name=""
class Player_Control:
    def __init__(self):
        self.setname()
        self.life = True
        self.cards = []
    def setname(self):
        global name
        print('請輸入玩家名稱')#what is your name?
        self.username = input()
        name=self.username
    
    def name(self):
        global name
        return name

    def join(self):
        print('是否加入此局？')#'join? y/n'
        print('加入請輸入y，拒絕加入請輸入n')
        if input() == 'y':
            return True
        return False

    def take(self,my_Cards):#my_Cards
        #global name
        #print(name + '目前手牌:', my_Cards,sep="")
        print('請問需要加牌嗎？')#'want more? y/n'
        print('需要請輸入y，不需要加入請輸入n')
        if input() == 'y':
            return True
        return False




count_com = 1
comname=""

class Computer_Control(Player_Control):
    
    def setname(self):
        global count_com,comname
        self.username='Computer'+str(count_com)
        count_com+=1
        comname=self.username
    def comname(self):
        global comname
        return comname

    def join(self):
        return True
        
    def take(self):
        if input() == 'y':
            return True
        return False




# {
#     "username": String # 玩家名稱,
#     "life": True|False,
#     "cards": [ Card, ...],
#     {"username": String}:{"life": True|False,"cards": [ Card, ...]}
#     # 是否下注
#     join() -> True|False # True: 下注
#     # 是否拿牌
#     take( my_cards ) -> True|False # True: 拿
#     # 遊戲事件
#     game_event( event )
# }


# event: {
#     "player": String     # 玩家名稱
#     "take":   True|False # 是否拿牌 True: 拿
#     "life":   True|False # 是否死亡 True: 生存
# }





def Test(Test_Data):
    if Test_Data.get("Hello", None) == True:
        return {"World": True}