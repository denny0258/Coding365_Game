# -*- coding: utf-8 -*-

from Model.c import settle_accounts

playernames = {}
player_count = 0
suit_to_num = {
    "s": 1,
    "h": 2,
    "d": 3,
    "c": 4
}


def setPlayers(players):
    index = 0

    player_count = len(players)
    settle_accounts.set_player_count(player_count)    

    for i in players:
        player = players[i]

        if not player.life:
            break

        # set card count and life status
        #   for each player, how many cards
        playernames[index] = i
        settle_accounts.set_card_count(index, len(player.cards), player.life)

        # set card
        card_index = 0
        for card in player.cards:
            settle_accounts.set_card(index, card_index, suit_to_num[card[0]], card[1])
            card_index+=1

        index+=1


def winner(players):
    result = {}
    for i in playernames:
        isWinner = settle_accounts.get_is_winner(i)
        result[playernames[i]] = isWinner
    return result

def Test(Test_Data):
    pass