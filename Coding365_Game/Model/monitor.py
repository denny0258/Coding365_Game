# -*- coding: utf-8 -*-
#如果爆炸就跳出

def Check_21(income):
    bool1=""
    dict1={}
    for j in income.keys():
        dict1[j]=bool1
        if income[j]["life"]=='False':
            dict1[j]="False"
        else:
            point=0
            for k in range(len(income[j]["Card"])):
                point+=(income[j]["Card"])[k][1]
                if point>21:
                    dict1[j]="False"
                else:
                    dict1[j]="True"
    return dict1
# e={"Player_1" : {"life":'False',"Card":[('s',2)]},"Player_2" : {"life":'True',"Card":[('s',3),('h',5),('d',6),('c',9)]},"Player_3" : {"life":'True',"Card":[('d',3),('h',4),('s',6),('c',7)]}}
# print(Check_21(e))
# f={"Player_1" : {"life":'False',"Card":[('s',7)]},"Player_2" : {"life":'True',"Card":[('s',4),('h',6),('d',7),('c',8)]},"Player_3" : {"life":'True',"Card":[('d',2),('s',3),('s',6),('c',6)]}}
# print(Check_21(f))

def Test(Test_Data):
   if Test_Data.get("Hello", None) == True:
       return {"World" : True}