# -*- coding: utf-8 -*-
# def Player_counts() :


def check_people():
    dict1 = {}
    print("Welcome ,please enter players number")
    P = int(input())
    print("Please enter computer players number")
<<<<<<< HEAD
    AI=int(input())
    print("Please enter computer players difficuilty (1~10)")
    dif=int(input())
    all_player = P + AI 
=======
    AI = int(input())
    all_player = P + AI
>>>>>>> 1d6219b79df3d206eaf5d75095c4756324178e86
    while all_player > 10:
        print("total player must less than 10,please enter again ")
        print("please enter players number")
        P = int(input())
        print("Please enter computer players number")
<<<<<<< HEAD
        AI=int(input())
        print("Please enter computer players difficuilty (1~10)")
        dif=int(input())
=======
        AI = int(input())
>>>>>>> 1d6219b79df3d206eaf5d75095c4756324178e86
        all_player = P + AI
        if all_player < 10:
            break
<<<<<<< HEAD
    dict1["player"]=P
    dict1["computer"]=AI
    dict1["difficuilty"]=dif
    return dict1
print(check_people())

#def Test(Test_Data):#
    #if Test_Data.get("Hello", None) == True:
    #return {"World" : True}
=======
    dict1["player"] = P
    dict1["computer"] = AI
    return dict1

>>>>>>> 1d6219b79df3d206eaf5d75095c4756324178e86

def Test_inside():
    print(check_people())


if __name__ == "__main__":
    Test_inside()


def Test(Test_Data):
    if Test_Data.get("Hello", None) == True:
        return {"World": True}
