# -*- coding: utf-8 -*-

dict1 = {}
playercount = 0
money = {}


def Get_Chip(income):
    global dict1, money
    money = {}
    for j in income.keys():
        if income[j] < 5:
            dict1[j] = False
        else:
            dict1[j] = True
            money[j] = income[j]
    return dict1


def Winner(winners):
    global playercount, money
    playercount = 0
    list1 = []
    for i in money.values():
        playercount += i

    dict2 = {}
    get_chip = []
    for i in (winners.values()):
        get_chip.append(i)
    winnercount = get_chip.count(True)
    average = playercount//winnercount
    for i in winners.keys():
        if winners[i] == True:
            dict2[i] = average
    return dict2


def Test_inside():
    # ------------------------------------------------------------
    income_1 = {"Player_1": 5, "Player_2": 5,
                "Player_3": 5, "Player_4": 5, "Player_5": 5}
    winners_1 = {'Player_1': False, 'Player_2': False,
                 'Player_3': False, 'Player_4': False, 'Player_5': True}
    # ------------------------------------------------------------
    income_2 = {"Player_1": 5, "Player_2": 5,
                "Player_3": 5, "Player_4": 5, "Player_5": 5}
    winners_2 = {'Player_1': False, 'Player_2': False,
                 'Player_3': False, 'Player_4': False, 'Player_5': True}
    # ------------------------------------------------------------
    income_3 = {"Player_1": 25, "Player_2": 35,
                "Player_3": 15, "Player_4": 2, "Player_5": 5}
    winners_3 = {'Player_1': False, 'Player_2': True,
                 'Player_3': False, 'Player_4': False, 'Player_5': True}
    # ------------------------------------------------------------

    print(Get_Chip(income_1))

    print(Winner(winners_1))
    # ------------------------------------------------------------

    print(Get_Chip(income_2))

    print(Winner(winners_2))
    # ------------------------------------------------------------

    print(Get_Chip(income_3))

    print(Winner(winners_3))


if __name__ == "__main__":
    Test_inside()


def Test(Test_Data):
    if Test_Data.get("Hello", None) == True:
        return {"World": True}