# -*- coding: utf-8 -*-
# def Player_counts() :


def check_people():
    dict1 = {}
    print("Welcome ,please enter players number")
    P = int(input())
    print("Please enter computer players number")
    AI = int(input())
    all_player = P + AI
    while all_player > 10:
        print("total player must less than 10,please enter again ")
        print("please enter players number")
        P = int(input())
        print("Please enter computer players number")
        AI = int(input())
        all_player = P + AI
        if all_player < 10:
            break
    dict1["player"] = P
    dict1["computer"] = AI
    return dict1


def Test_inside():
    print(check_people())


if __name__ == "__main__":
    Test_inside()


def Test(Test_Data):
    if Test_Data.get("Hello", None) == True:
        return {"World": True}
