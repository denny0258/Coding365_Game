# -*- coding: utf-8 -*-

# 發牌 陳敦捷
# python c 對接 邱柏翰

try:
    from Model.C_Data import shuffle
except:
    try:
        from C_Data import shuffle
    except:
        try:
            from Model.C_Data import shuffle_fallback as shuffle
        except:
            from C_Data import shuffle_fallback as shuffle

def Take_card(inputs):
    card = shuffle.Take_Card(inputs["RE"])
    return {"Card": card}

def Test(Test_Data):
    if Test_Data.get("Hello", None) == True:
        return {"World": True}
