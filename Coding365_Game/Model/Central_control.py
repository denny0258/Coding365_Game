# -*- coding: utf-8 -*-
# ------------------------------------

import os
import Chip
import deal
import money
import people
import example
import monitor
import Leaderboard
import Central_control
import settle_accounts
import Player_Control

print_Data = ""
difficuilty = 0
# =====================================


def start():
    global print_Data
    os.system("cls")
    players = Setup_Peoples()
    os.system("PAUSE")
    os.system("cls")
    while True:
        players = Join_Game(players)
        Start_Game(players)
        print("是否在玩下一局? (y/n)")
        print_Data = ""
        if input().strip().lower() == 'y':
            pass
            os.system("cls")
        else:
            break
    print("end")
# =====================================


def Setup_Peoples():
    global difficuilty
    people_Ok = True
    while people_Ok:
        people_info = people.check_people()
        print('請確認玩家數量為：', people_info["player"], "\n電腦數量為：",
              people_info["computer"],  "\n是否正確：(y/n)", end="")
        if input() == "y":
            people_Ok = False
    os.system("cls")
    players = [Player_Control.Player_Control()
               for i in range(people_info["player"])]
    players += [Player_Control.Computer_Control()
                for i in range(people_info["computer"])]
    print("===================================\n\n準備完成!\n\n===================================")
    difficuilty = people_info["difficuilty"]
    return players

# =====================================


def Join_Game(players):
    remove_these_peoples = []
    for player in players:
        print("玩家：", player.name, "\t\n您有:",
              money.Get_money([player.id])[player.id], "元的籌碼")
        if player.join():
            player.cards = []
            player.life = True
            if money.Get_money([player.id])[player.id] < 5:
                print("玩家：", player.name, "\n入桌費金額不足無法參加(入桌費5元)")
                remove_these_peoples.append(player)
                os.system("PAUSE")
                os.system("cls")
                continue
            # -------------------------------------
            while player.name.find("Computer") == -1:
                chip_money = float(input("請下注(最低下注金額5元):"))
                if chip_money > 5 and money.Get_money([player.id])[player.id] >= chip_money:
                    Chip.Get_Chip({player.id: chip_money})
                    money.Take_money({player.id: chip_money})
                    break
                else:
                    print("不足5元或下注金額大於擁有金額")
            print("玩家：", player.name, '\n連線成功!')
            # -------------------------------------
            if player.name.find("Computer") != -1:
                Chip.Get_Chip({player.id: 5})
                money.Take_money({player.id: 5})
            else:
                os.system("PAUSE")
            os.system("cls")

    return [player for player in players if player not in remove_these_peoples]

# =====================================


def Get_public_Card(players):
    global print_Data
    print("向各玩家分別派發一張明牌\n\n====================================\n")
    print_Data += "===========================各自的明牌如下===========================\n"
    deal.Take_card({"RE": True})  # 洗牌
    for player in players:
        os.system("cls")
        print(print_Data)
        card = deal.Take_card({"RE": False})["Card"]
        player.add_card(card)
        print_Data += str(player.name) + "的明牌為：" + \
            str(Player_Control.card_to_str(card)) + "\n"
    print_Data += "===========================各自的狀態如下===========================\n"

# =====================================


def Want_Get(player):
    global print_Data, difficuilty
    if player.take(difficuilty):
        card = deal.Take_card({"RE": False})["Card"]
        if card == None:
            return "Nocard"
        player.add_card(card)
        player.life = monitor.Check_21({
            player.id: {
                "life": player.life,
                "cards": player.cards
            }
        })[player.id]
        if player.life == False:
            print(player.name, "爆炸了: ")
            print("你的卡片：", player.my_cards())
            print_Data += player.name + "已死亡\n"
            os.system("PAUSE")
            return "Dead"
        else:
            return None
    else:
        print_Data += player.name + "已喊停\n"
        return "stop"

# =====================================
# =====================================
# =====================================


def Start_Game(players):
    global print_Data
    Get_public_Card(players)
    # ---------------------------------
    skip_list = list()
    status_temp = set()
    count = 0
    # ---------------------------------
    while len(skip_list) != len(players) and count != -1:
        count += 1
        for player in players:
            os.system("cls")
            print("第", count, "回")
            print(print_Data, "\n\n\n\n")
            if player.id not in skip_list:
                status = Want_Get(player)
                if status == "stop" or status == "Dead":
                    skip_list.append(player.id)
                    status_temp.add(status)
                elif (status == "Nocard") or (len(players) - len(skip_list) == 1 and status_temp == 1):
                    count = -1
                    break
    print_Data = ""
    # ---------------------------------
    winners = settle_accounts.winner(
        {player.id: {"life": player.life, "cards": player.cards}for player in players})
    chips = Chip.Winner(winners)
    money.Add_money(chips)
    # ---------------------------------
    for player in players:
        if winners[player.id]:
            print(player.name, "贏了耶")
            print("贏得", chips[player.id], "籌碼!")
            print("現在總共有", money.Get_money([player.id])[player.id], "籌碼!")

    print("===========================遊戲結束=========================")


def Test(Test_Data):
    if Test_Data.get("Hello", None) == True:
        return {"World": True}
