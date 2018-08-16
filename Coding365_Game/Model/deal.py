# -*- coding: utf-8 -*-

#發牌 陳敦捷
#python c 對接 邱柏翰
from Adapter import cAdapter
import os

deal_module = cAdapter.GetAdapter(os.path.abspath("./model/deal.exe"))
shuffle_module = cAdapter.GetAdapter(os.path.abspath("./model/shuffle.exe"))
shuffle_module.start()

def Take_card(inputs):

    if inputs["RE"]:
        shuffle_module.stop()
        shuffle_module.start()

    Card_str = shuffle_module.call('B')
    Card_suit = Card_str[2]
    Card_num = Card_str.split(',')[1][:-1]
    print('card debug', Card_suit, Card_num)
    return (Card_suit, Card_num)

def Test(Test_Data):
    global deal_module
    s = ''
    for i in Test_Data:
        if Test_Data[i]:
            s+=i
    
    deal_module.start()
    result = deal_module.call(s)
    deal_module.stop()
    d = {}
    d[result] = True
    # print('debug from deal: result:', d)
    return d