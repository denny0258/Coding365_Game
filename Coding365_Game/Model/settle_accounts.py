# -*- coding: utf-8 -*-

try:
    from Model.C_Data import winner as winner_c_module
except:
    try:
        from C_Data import winner as winner_c_module
    except:
        try:
            from Model.C_Data import winner_fallback as winner_c_module
        except:
            from C_Data import winner_fallback as winner_c_module
        


def setPlayers(players):

    playernames = {}  # { player_id: player_name , ... }

    suit_to_num = {
        "s": 1,
        "h": 2,
        "d": 3,
        "c": 4
    }

    index = 0

    player_count = len(players)
    winner_c_module.set_player_count(player_count)

    for i in players:
        player = players[i]

        # set card count and life status
        #   for each player, how many cards
        playernames[index] = i
        winner_c_module.set_card_count(
            index, len(player["cards"]), 1 if player["life"] else 0)

        
        # set card
        card_index = 0
        for card in player["cards"]:
            winner_c_module.set_card(
                index, card_index, suit_to_num[card[0]], card[1])
            # print(index, card_index, suit_to_num[card[0]], card[1])
            card_index += 1

        index += 1

    return playernames


def winner(players):
    playernames = setPlayers(players)
    winner_c_module.winner()
    result = {}
    for i in playernames:
        isWinner = winner_c_module.get_is_winner(i)
        result[playernames[i]] = isWinner == 1
    return result


def Test(Test_Data):
    if Test_Data.get("Hello", None) == True:
        return {"World": True}


def Test_Self():
    input_data = {
        "P2": {
            "life": True,
            "cards": [('h', 13), ('d',13) ]
        },
         "P1": {
            "life": True,
            "cards": [('s', 1), ('h', 2), ('d', 3), ('c', 13)]
        }
    }

    print(winner(input_data))
    print(winner_c_module.get_max_point())


if __name__ == '__main__':
    Test_Self()
