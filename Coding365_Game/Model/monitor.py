# -*- coding: utf-8 -*-
# 如果爆炸就跳出


def Check_21(income):
    bool1 = ""
    dict1 = {}
    for j in income.keys():
        dict1[j] = bool1
        if income[j]["life"] == False:
            dict1[j] = False
        else:
            point = 0
            for k in range(len(income[j]["cards"])):
                if (income[j]["cards"])[k][1] > 10:
                    point += 10
                else:
                    point += (income[j]["cards"])[k][1]
                if point > 21:
                    dict1[j] = False
                else:
                    dict1[j] = True
    return dict1

def Test(Test_Data):
    if Test_Data.get("Hello", None) == True:
        return {"World": True}
