# -*- coding: utf-8 -*-


def hand(card, difficuilty):
    if sum([i[1] for i in card]) < difficuilty*2:
        return True
    else:
        return False


def Test(Test_Data):
    if Test_Data.get("Hello", None) == True:
        return {"World": True}
