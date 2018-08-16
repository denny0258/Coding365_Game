# -*- coding: utf-8 -*-
# def Player_counts() :
#     players = int(input())
#     return players

def Get_people():
    total = int(input())    
    while total > 10 :
        total=int(input())
    players = int(input())
    computer= total-players
    dict1={}
    dict1["Player_counts"]=players
    dict2={}
    dict2["computer_counts"]=computer
    return dict1



#def computer_counts(Get_people) :
    # computer= total-players
    # return computer
# def Test(Test_Data):
#    if Test_Data.get("Hello", None) == True:
#        return {"World" : True}

print(Get_people())


