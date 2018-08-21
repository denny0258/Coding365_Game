

class Player:
    def __init__(self):
        self.username = 'test'
        self.life = True
        self.cards = []

    def join(self):
        return True

    def take(self, myCards):
        print(myCards)
        return True

    def gameEvent(self, event):
        print(event)


'''
{
    "username": String # 玩家名稱
    "life": True|False,
    "cards": [ Card, ...],
    
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
'''
