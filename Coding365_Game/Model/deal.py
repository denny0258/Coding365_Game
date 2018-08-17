# -*- coding: utf-8 -*-

#發牌 陳敦捷
#python c 對接 邱柏翰

from Model.c import shuffle

def Take_card(inputs):
    card = shuffle.Take_Card(inputs["RE"])
    return {"Card": card}


# 先亂寫的
def Test(Test_Data):
    return "World"