# -*- coding: utf-8 -*-
dict1={}
playercount=0
money={}

def Get_Chip(income):
    global dict1,money
    money={}
    for j in income.keys():
        if income[j]<5:
            dict1[j]=False
        else:
            dict1[j]=True
            money[j]=income[j]
    return dict1

def Winner(winners):
    global playercount,money
    playercount=0
    list1=[]
    for i in money.values():
        playercount+=i

    dict2={}
    get_chip=[]
    for i in (winners.values()):
        get_chip.append(i)
    winnercount=get_chip.count(True)
    average=playercount//winnercount
    for i in winners.keys():
        if winners[i]==True:
            dict2[i]=average
    return dict2


# income={"Player_1":5,"Player_2":5,"Player_3":5,"Player_4":5,"Player_5":5}
# winners={'Player_1': False, 'Player_2': False, 'Player_3': False, 'Player_4': False, 'Player_5': True}
# print(Get_Chip(income))
# print(Winner(winners))
# print()

# income1={"Player_1":25,"Player_2":35,"Player_3":15,"Player_4":2,"Player_5":5}
# winners1={'Player_1': False, 'Player_2': True, 'Player_3': False, 'Player_4': False, 'Player_5': True}
# print(Get_Chip(income1))
# print(Winner(winners1))

def Test(Test_Data):
    if Test_Data.get("Hello", None) == True:
        return {"World": True}