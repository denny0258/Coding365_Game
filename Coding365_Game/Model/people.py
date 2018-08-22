# -*- coding: utf-8 -*-


def check_people():
    dict1 = {}
    print("Welcome ,please enter players number")
    P = int(input())
    print("Please enter computer players number")
    AI = int(input())
    print("Please enter computer players difficuilty (1~10)")
    dif = int(input())
    all_player = P + AI
    while all_player > 10:
        print("total player must less than 10,please enter again ")
        print("please enter players number")
        P = int(input())
        print("Please enter computer players number")
        AI = int(input())
        print("Please enter computer players difficuilty (1~10)")
        dif = int(input())
        all_player = P + AI
        if all_player < 10:
            break
    dict1["player"] = P
    dict1["computer"] = AI
    dict1["difficuilty"] = dif
    return dict1


def Test(Test_Data):
    if Test_Data.get("Hello", None) == True:
        return {"World": True}