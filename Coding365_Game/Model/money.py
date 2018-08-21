# -*- coding: utf-8 -*-
# 金錢系統

people_Account = {}


def Get_money(people):
    global people_Account
    [people_Account.update({key: people_Account.get(key, 50)})
     for key in people]
    return({i: people_Account.get(i, 50) for i in people})


def Add_money(delta_Money_1):
    global people_Account
    [people_Account.update({key: people_Account.get(key, 0) + value})
     for key, value in delta_Money_1.items()]


def Take_money(withdraw_1):
    global people_Account
    A = {}
    for k, v in withdraw_1.items():
        result = people_Account.get(k, 50) - v
        if result < 0:
            A.update({k: False})
        else:
            people_Account[k] = result
            A.update({k: True})

    return A


def Test(Test_Data):
    if Test_Data.get("Hello", None) == True:
        return {"World": True}
