# -*- coding: utf-8 -*-

#發牌 陳敦捷
#python c 對接 邱柏翰
from Adapter import cAdapter
import os

def Take_card():
    pass

def Test(Test_Data):
    s = ''
    for i in Test_Data:
        if Test_Data[i]:
            s+=i
    adapter = cAdapter.GetAdapter(os.path.abspath("./model/deal.exe"))
    adapter.start()
    result = adapter.call(s+'\r\n').strip()
    adapter.stop()
    d = {}
    d[result] = True
    print('debug from deal: result:', d)
    return d