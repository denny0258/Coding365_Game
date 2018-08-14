# -*- coding: utf-8 -*-
#如果爆炸就跳出

def Check_21(e):
    a=0
    b=""
    dict1={}
    for j in e.keys():
        dict1[j]=b
        if e[j]["life"]==False:
            dict1[j]="False"
        else:
            for k in range(len(e[j]["Card"])):
                a+=(e[j]["Card"])[k]
                if a>21:
                    dict1[j]="False"
                else:
                    dict1[j]="True"
return dict1

# def Test(Test_Data):
#    pass
# def Test(Test_Data):
#    if Test_Data.get("Hello", None) == True:
#        return {"World" : True}