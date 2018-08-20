# -*- coding: utf-8 -*-
# 金錢系統

peoples = ["Player_1","Player_2","Player_3","Player_4"]  #最一開始的人
delta_Money = {"Player_3":75}   #贏得總量
withdraw = {"Player_1": -60, "Player_2": -25, "Player_3": -15, "Player_4": -55}

people_Account = {}

def Get_money(people):
    global people_Account
    [people_Account.update({key: people_Account.get(key, 50)}) for key in people]
    return(people_Account)

def Add_money(delta_Money_1):
    global people_Account
    [people_Account.update({key: people_Account.get(key, 0) + delta_Money_1.get(key, 0)}) for key, value in people_Account.items()]
    
def Take_money(withdraw_1):
    global people_Account
    A = {}
    for k,v in withdraw_1.items():
        if people_Account.get(k,50) + v < 0:
            A.update({k:False})
        else:
            A.update({k:True})

    return A

    
if __name__ == "__main__":
    print(Get_money(peoples))
    print(Add_money(delta_Money))
    print(Take_money(withdraw))



def Test(Test_Data):
    if Test_Data.get("Hello", None) == True:
        return {"World": True}
