# -*- coding: utf-8 -*-
import pprint

Datas = dict()


def Record(records):
    global Datas

    def record_func(Key, Value):
        Datas[Key]["money"] = Value["money"]
        if Value["win"]:
            Datas[Key]["win_counts"] = 1 + Datas[Key].get("win_counts", 0)
        else:
            Datas[Key]["defeat_counts"] = 1 + \
                Datas[Key].get("defeat_counts", 0)
        Datas[Key]["cards"] = Datas[Key].get(
            "cards", []) + [Value["cards"]]

    for Key, Value in records.items():
        Datas[Key] = Datas.get(Key, dict())
        record_func(Key, Value)


def Get_Leader():
    global Datas
    return_Data = dict()

    def Get_rate(Value):
        if Value.get("win_counts", 0) + Value.get("defeat_counts", 0) == 0:
            return 0
        return int(Value.get("win_counts", 0) / (Value.get("win_counts", 0) + Value.get("defeat_counts", 0))*100)
    for Key, Value in Datas.items():
        return_Data[Key] = {"money": Value.get("money", 0), "win_rate": Get_rate(
            Value), "win": Value.get("win_counts", 0), "defeat": Value.get("defeat_counts", 0)}

    return return_Data


def Tset_insid():
    print(Get_Leader())

    Test_Data_1 = {
        "Player_1": {
            "money": 20,
            "win": False,
            "cards": [("p", 7), ("l", 10), ("s", 10)]
        }, "Player_2": {
            "money": 30,
            "win": True,
            "cards": [("k", 7), ("l", 8), ("a", 2), ("t", 3)]
        }
    }

    Record(Test_Data_1)
    print(Get_Leader())

    Test_Data_2 = {
        "Player_1": {
            "money": 50,
            "win": True,
            "cards": [("p", 5), ("l", 2), ("s", 9)]
        }, "Player_2": {
            "money": 25,
            "win": False,
            "cards": [("k", 8), ("l", 8), ("a", 4), ("t", 3)]
        }, "Player_3": {
            "money": 45,
            "win": False,
            "cards": [("k", 8), ("l", 7), ("a", 9), ("t", 5)]
        }, "Player_4": {
            "money": 5,
            "win": True,
            "cards": [("k", 2), ("l", 7), ("a", 4), ("t", 3)]
        }
    }
    Record(Test_Data_2)
    print(Get_Leader())

    Test_Data_3 = {
        "Player_1": {
            "money": 25,
            "win": False,
            "cards": [("p", 7), ("l", 9), ("s", 10)]
        }, "Player_2": {
            "money": 35,
            "win": True,
            "cards": [("k", 7), ("l", 8), ("a", 2), ("t", 3)]
        }, "Player_3": {
            "money": 15,
            "win": True,
            "cards": [("k", 7), ("l", 4), ("a", 2), ("t", 3)]
        }
    }
    Record(Test_Data_3)

    print(Get_Leader())


Tset_insid()


def Test(Test_Data):
    if Test_Data.get("Hello", None) == True:
        return {"World": True}
