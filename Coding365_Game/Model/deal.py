# -*- coding: utf-8 -*-

#發牌 陳敦捷
#python c 對接 邱柏翰

from Model.c import test



def Take_card(inputs):
    if inputs["RE"]:
        test.shuffle()
    
    card = test.get()
    return {"Card": card}





# 先亂寫的
def Test(Test_Data):
    return "World"