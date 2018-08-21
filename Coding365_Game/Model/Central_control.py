# -*- coding: utf-8 -*-
# ------------------------------------

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
import Player_Control


def start():

    players = setup_peoples()

    while True:
        players = join_game(players)
        start_game(players)

        print("go go next round? (y/n)")
        if input().strip().lower() == 'y':
            pass
        else:
            break


def setup_peoples():
    players = []

    people_info = people.check_people()

    for i in range(people_info["player"]):
        players.append(Player_Control.Player_Control())

    for i in range(people_info["computer"]):
        players.append(Player_Control.Computer_Control())

    print("OK, Game start!")
    return players


def join_game(players):
    remove_these_peoples = []

    players_list = [player.id for player in players]
    money_list = money.Get_money(players_list)
    for player in players:
        print(player.name, "\tyou have:", money_list[player.id])

        if player.join():
            query = {}
            query[player.id] = 5
            result = money.Take_money(query)[player.id]

            if result:
                print(player.name, 'joined!')
            else:
                print(player.name, "your money not enough")
                remove_these_peoples.append(player)

    return [player for player in players if player not in remove_these_peoples]


def start_game(players):
    # game start!
    game_running = True
    need_shuffle = True

    print("all player will get one card public, one card private")

    for player in players:
        card = deal.Take_card({"RE": need_shuffle})["Card"]
        need_shuffle = False
        print(player.name, "public card", card)
        player.add_card(card)

    for player in players:
        card = deal.Take_card({"RE": need_shuffle})["Card"]
        player.add_card(card)

    print("all players now have two cards.")

    # now enter game loop

    while True:

        skip_list = []
        need_take_card = True
        card = None

        this_round_have_people = False

        for player in players:

            if player in skip_list:
                continue

            if need_take_card:
                card = deal.Take_card({"RE": False})["Card"]
                need_take_card = False

            if card is None:
                # no card, game ended
                game_running = False
                break

            this_round_have_people = True

            if player.take():
                player.add_card(card)
                need_take_card = True

                life_result = monitor.Check_21({
                    "p": {
                        "life": player.life,
                        "cards": player.cards
                    }
                })["p"]

                if life_result == False:
                    print("爆炸拉: ", player.name)
                    print("the cards: ", player.my_cards())
                    player.life = False

            else:
                skip_list.append(player)

        if not this_round_have_people:
            game_running = False

        if not game_running:
            break

    # now find winner

    players_list = {}
    query = {}

    for player in players:
        players_list[player.id] = player

    for player in players:
        query[player.id] = {
            "life": player.life,
            "cards": player.cards
        }

    winners = settle_accounts.winner(query)
    chips = Chip.Winner(winners)
    money.Add_money(chips)

    for i in players_list:
        player = players_list[i]
        if winners[i]:
            print(player.name, "贏了耶")
            print(" 贏得", chips[i], "籌碼!")
            print(" 現在總共有", money.Get_money([i])[i], "籌碼!")
    
    print("遊戲結束")


def Test(Test_Data):
    pass


start()
