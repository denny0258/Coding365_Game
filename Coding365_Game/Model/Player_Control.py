def card_to_str(card):
    s=''
    if card[0]=="s":
        s+="黑桃"
    elif card[0]=="h":
        s+="紅桃"
    elif card[0]=="d":
        s+="方塊"
    else:
        s+="梅花"

    if card[1]==1:
        s+="A"
    elif card[1]==11:
        s+="J"
    elif card[1]==12:
        s+="Q"
    elif card[1]==13:
        s+="K"
    else:
        s+=str(card[1])
    return s

count_pla=1
class Player_Control:
    def __init__(self):
        self.name = ''
        self.setname()
        self.life = True
        self.cards = []

    def setname(self):
        global count_pla
        print('請輸入玩家名稱')#what is your name?
        self.name = input()
        self.id = "player_"+str(count_pla)
        count_pla+=1
    
    def join(self):
        print('是否加入此局？')#'join? y/n'
        print('加入請輸入y，拒絕加入請輸入n')
        if input() == 'y':
            return True
        return False

    def my_cards(self):
        owncard=""
        for i in range(len(self.cards)):
            owncard+=self.cards+" "
        return owncard

    def take(self):#my_Cards
        print(self.name + '目前手牌:', self.my_cards(),sep="")
        print(self.name,'請問需要加牌嗎？')#'want more? y/n'
        print('需要請輸入y，不需要加入請輸入n')
        if input() == 'y':
            return True
        return False

    def game_event(self,event):
        print(self.name,end="")
        if event["life"]==False:
            print("已死亡")
        else:
            if event[i]["take"]==True:
                print("選擇加一張牌")
            else:
                print("選擇不加牌")
    
    def add_card(self, card):
        print(self.name,"獲得",end="")
        print(card_to_str(card))
        self.cards.append(card)



count_com = 1
class Computer_Control(Player_Control):
    
    def setname(self):
        global count_com
        self.name='Computer'+str(count_com)
        self.id = "computer_"+str(count_com)
        count_com+=1
        
    def join(self):
        return True
        
    def take(self):
        if input() == 'y':
            return True
        return False

    def add_card(self, card):
        self.cards.append(card)



def Test(Test_Data):
    if Test_Data.get("Hello", None) == True:
        return {"World": True}