# -*- coding: utf-8 -*-
# 金錢系統``

from operator import add
from operator import sub
from functools import reduce


def Get_Chip():  # 模擬下注 function
    return{
        'player_1': {'Chip': 1, 'InitChip': 10},
        'player_2': {'Chip': 2, 'InitChip': 10},
        'player_3': {'Chip': 3, 'InitChip': 10},
    }


def settle_accounts():  # 模擬勝負結算 function
    return{
        'Win': 'player_1'
    }


def Get_money():
    Chip_Remain = {}
    [Chip_Remain.update({key: value['InitChip'] - value['Chip']})for key, value in Get_Chip().items()]
    [Chip_Remain.update({key: value + reduce(add, [chip['Chip'] for chip in Get_Chip().values()])})for key, value in Chip_Remain.items()if settle_accounts()['Win'] in key]
    return(Chip_Remain)


if __name__ == '__main__':
    Get_money()

    print(Get_money())


def Test(Test_Data):
    if Test_Data.get("Hello", None) == True:
        return {"World": True}
