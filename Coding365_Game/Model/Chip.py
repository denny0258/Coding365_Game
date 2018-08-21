dict1 = {}
playercount = 0
money = {}


def Get_Chip(income):
    global dict1, money
    for j in income.keys():
        if income[j] < 5:
            dict1[j] = False
        else:
            dict1[j] = True
            money[j] = income[j]
    return dict1


def Winner(winners):
    global money
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
    money = {}
    return dict2

def Test(Test_Data):
    if Test_Data.get("Hello", None) == True:
        return {"World": True}
