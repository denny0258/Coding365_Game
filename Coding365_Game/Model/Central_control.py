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
from pprint import pprint


def start():

    players = setup_peoples()
    
    while True:
        players = join_game(players)
        start_game(players)

        pprint("go go next round? (y/n)")
        if input().strip().lower() == 'y':
            pass
        else:
            break
        

def setup_peoples():
    players = []
    need_shuffle = True

    people_info = people.check_people()

    for i in range(people_info["player"]):
        players.append(Player_Control.Player_Control())

    for i in range(people_info["computer"]):
        players.append(Player_Control.Computer_Control())

    pprint("OK, Game start!")
    return players


def join_game(players):
    remove_these_peoples = []

    players_list = [player.id for player in players]
    money_list = money.Get_money(players_list)
    for player in players:
        pprint(player.name, "\tyou have:", money_list[player.id])

        if player.join():
            query = {}
            query[player.id] = 5
            result = money.Take_money(query)[player.id]

            if result:
                pprint(player.name, 'joined!')
            else:
                pprint(player.name, "your money not enough")
                remove_these_peoples.append(player)
    
    return [player for player in player if player not in remove_these_peoples]


def start_game(players):
    # game start!
    game_running = True

    pprint("all player will get one card public, one card private")

    for player in players:
        card = deal.Take_card({"RE": need_shuffle})["Card"]
        need_shuffle = False
        pprint(player.name, "public card", card)
        player.add_card(card)

    for player in players:
        card = deal.Take_card({"RE": need_shuffle})["Card"]
        player.add_card(card)

    pprint("all players now have two cards.")

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

            if player.take(player.cards):
                player.cards.add_card(card)
                need_take_card = True

                life_result = monitor.Check_21({
                    "p": {
                        "life": player.life,
                        "cards": player.cards
                    }
                })["p"]

                if life_result == False:
                    pprint("player over 21 point: ", player.name)
                    pprint("the card he has: ", player.my_cards())
                    player.life = False


            else:
                skip_list.append(player)

        if not this_round_have_people:
            game_running = False

        if not game_running:
            break

    # now find winner

    players_list = []

    for player in players:
        players_list.append({
            "life": player.life,
            "cards": player.cards
        })

    winners = settle_accounts.winner(players_list)


def Test(Test_Data):
    pass


start()