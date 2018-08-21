# -*- coding: utf-8 -*-
import os
import Chip
import deal
import money
import people
import example
import monitor
import computer_AI
import Leaderboard
import Central_control
import settle_accounts
from pprint import pprint

from print_API import printAPI, inputAPI

# ----------------------------------------------------------------------------


def Test_process():
    print("\n\n=====================================================\n\n")
    print("\n現在測試 Chip\n")
    Test_Chip()
    print("\n\n=====================================================\n\n")
    print("\n現在測試 monitor\n")
    Test_monitor()
    print("\n\n=====================================================\n\n")
    print("\n現在測試 deal\n")
    Test_deal()
    print("\n\n=====================================================\n\n")
    print("\n現在測試 people\n")
    Test_people()


# ========================================


def Test_people():
    print(people.check_people())

# ========================================


def Test_monitor():
    # ------------------------------------------------------------
    Data_1 = {"Player_1": {"life": False, "Card": [('s', 2)]},
              "Player_2": {"life": True, "Card": [('s', 3), ('h', 5), ('d', 6), ('c', 9)]},
              "Player_3": {"life": True, "Card": [('d', 3), ('h', 4), ('s', 6), ('c', 7)]},
              "Player_4": {"life": True, "Card": [('d', 7), ('s', 3), ('s', 7), ('c', 3)]},
              "Player_5": {"life": True, "Card": [('d', 13), ('s', 6), ('s', 5), ('c', 8)]}
              }
    # ------------------------------------------------------------
    Data_2 = {"Player_1": {"life": False, "Card": [('s', 7)]},
              "Player_2": {"life": True, "Card": [('s', 4), ('h', 6), ('d', 7), ('c', 8)]},
              "Player_3": {"life": True, "Card": [('d', 2), ('s', 3), ('s', 6), ('c', 6)]}
              }
    print("測試資料 1:")
    pprint(Data_1)
    print("測試結果 1:", monitor.Check_21(Data_1), sep="\n")
    print("\n測試資料 2:")
    pprint(Data_2)
    print("測試結果 2:", monitor.Check_21(Data_2), sep="\n")

# ========================================


def Test_Chip():
    # ------------------------------------------------------------
    income_1 = {"Player_1": 5, "Player_2": 5,
                "Player_3": 5, "Player_4": 5, "Player_5": 5}
    winners_1 = {'Player_1': False, 'Player_2': False,
                 'Player_3': False, 'Player_4': False, 'Player_5': True}
    # ------------------------------------------------------------
    income_2 = {"Player_1": 5, "Player_2": 5,
                "Player_3": 5, "Player_4": 5, "Player_5": 5}
    winners_2 = {'Player_1': False, 'Player_2': False,
                 'Player_3': False, 'Player_4': False, 'Player_5': True}
    # ------------------------------------------------------------
    income_3 = {"Player_1": 25, "Player_2": 35,
                "Player_3": 15, "Player_4": 2, "Player_5": 5}
    winners_3 = {'Player_1': False, 'Player_2': True,
                 'Player_3': False, 'Player_4': False, 'Player_5': True}
    # ------------------------------------------------------------

    print("income測試資料 1:", income_1, "income測試結果 1:",
          Chip.Get_Chip(income_1), "\n", sep="\n")

    print("winner測試資料 1:", winners_1, "winner測試結果 1:",
          Chip.Winner(winners_1), "\n", sep="\n")

    # ------------------------------------------------------------

    print("income測試資料 2:", income_2, "income測試結果 2:",
          Chip.Get_Chip(income_2), "\n", sep="\n")

    print("winner測試資料 2:", winners_2, "winner測試結果 2:",
          Chip.Winner(winners_2), "\n", sep="\n")

    # ------------------------------------------------------------
    print("income測試資料 3:", income_3, "income測試結果 3:",
          Chip.Get_Chip(income_3), "\n", sep="\n")

    print("winner測試資料 3:", winners_3, "winner測試結果 3:",
          Chip.Winner(winners_3), "\n", sep="\n")

# ========================================

# 測試 發牌模組
# 測試項目：
# 1. 初始洗牌一次，發52張牌
#       - 確認52張牌剛好都出現一次
# 2. 52 張牌後應該顯示 None 表示沒牌
# 3. 重新洗牌後再進行一次步驟 1 確定可重複洗牌發牌
# return True: 測試通過  False: 測試失敗


def Test_deal():
    for times in range(3):  # 總共進行三次測試
        re = True  # 是否需要洗牌
        cards = []  # 儲存所有牌面

        try:
            for i in range(52):
                card = deal.Take_card({"RE": re})["Card"]
                re = False
                cards.append(card)
        except:
            print('發牌過程發生例外導致測試失敗，目前牌面陣列：')
            print(cards)
            return False

        # 計算各種花色數量
        counts = {
            "s": [0]*14,
            "h": [0]*14,
            "d": [0]*14,
            "c": [0]*14,
        }

        for card in cards:
            suit = card[0]
            number = card[1]

            if suit not in counts:
                print('牌面花色錯誤導致測試失敗:', suit)
                return False

            if number < 0 or number > 13:
                print('牌面數字範圍錯誤導致測試失敗：', number)
                return False

            counts[suit][number] += 1

        count_pass = True
        for suit in counts:
            count = counts[suit]
            for i in range(1, 13+1):
                n = count[i]
                if n != 1:
                    print('牌數量有誤：', suit, i, '數量:', n)
                    count_pass = False

        if not count_pass:
            print('牌面有誤，測試失敗')
            return False

        for i in range(5):  # 不洗牌嘗試取得5張牌
            try:
                no_card = deal.Take_card({"RE": False})["Card"]
                if no_card is not None:
                    print('發完牌並沒有回傳 None ，測試失敗')
                    return False
            except:
                print('嘗試在發完牌後要牌發生例外，測試失敗')
                return False

        print("測試結果", times+1, ":")
        pprint(cards)

    return True
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


def Test():
    os.system("color 0C")
    print("\n\n==========請參考 example.py 確保自己開發的部分沒有 ERROR的訊息。==========\n\n")
    os.system("PAUSE && color 07")

    Test_Data = {"Hello": True}
    try:
        if example.Test(Test_Data).get("World", False) != True:
            printAPI("ERROR to example")
    except:
        printAPI("ERROR to example")
    # ================================================================
    try:
        if Central_control.Test(Test_Data).get("World", False) != True:
            printAPI("ERROR to Central_control")
    except:
        printAPI("ERROR to Central_control")
    # ================================================================
    try:
        if Chip.Test(Test_Data).get("World", False) != True:
            printAPI("ERROR to Chip")
    except:
        printAPI("ERROR to Chip")
    # ================================================================
    try:
        if deal.Test(Test_Data).get("World", False) != True:
            printAPI("ERROR to deal")
    except:
        printAPI("ERROR to deal")
    # ================================================================
    try:
        if money.Test(Test_Data).get("World", False) != True:
            printAPI("ERROR to money")
    except:
        printAPI("ERROR to money")
    # ================================================================
    try:
        if people.Test(Test_Data).get("World", False) != True:
            printAPI("ERROR to people")
    except:
        printAPI("ERROR to people")
    # ================================================================
    try:
        if monitor.Test(Test_Data).get("World", False) != True:
            printAPI("ERROR to monitor")
    except:
        printAPI("ERROR to monitor")
    # ================================================================
    try:
        if computer_AI.Test(Test_Data).get("World", False) != True:
            printAPI("ERROR to computer_AI")
    except:
        printAPI("ERROR to computer_AI")
    # ================================================================
    try:
        if settle_accounts.Test(Test_Data).get("World", False) != True:
            printAPI("ERROR to settle_accounts")
    except:
        printAPI("ERROR to settle_accounts")
    # ================================================================
    try:
        if Leaderboard.Test(Test_Data).get("World", False) != True:
            printAPI("ERROR to Leaderboard")
    except:
        printAPI("ERROR to Leaderboard")
    # ================================================================
