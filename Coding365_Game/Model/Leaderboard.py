# -*- coding: utf-8 -*-
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


def Test(Test_Data):
    if Test_Data.get("Hello", None) == True:
        return {"World": True}
