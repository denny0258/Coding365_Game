

play_num = 0  # 玩家數量
get = 0
max_point = 0

'''
struct card_t:
   suit 
   number 

'''
play_info = []
for i in range(20):
    info = {
        "life": True,  # 玩家是否生存
        "winner": False,  # 是否是贏家
        "sum": 0,  # 玩家手牌點數和
        "count": 0,  # 玩家持有牌數
        "card": []
    }

    for j in range(20):
        info["card"].append({
            "suit": 0,
            "number": 0
        })

    play_info.append(info)


def set_player_count(count):
    global play_num
    play_num = count


def set_card_count(pid, count, life):
    global play_info
    play_info[pid]["count"] = count
    play_info[pid]["winner"] = 0
    play_info[pid]["life"] = life


def set_card(pid, cid, suit, number):
    global play_info
    play_info[pid]["card"][cid]["suit"] = suit
    play_info[pid]["card"][cid]["number"] = number


def sum(pid, count):
    global play_info
    play_info[pid]["sum"] = 0

    for i in range(count):
        if play_info[pid]["card"][i]["number"] >= 10:
            play_info[pid]["sum"] += 10
        else:
            play_info[pid]["sum"] += play_info[pid]["card"][i]["number"]


def sum_total():
    global play_num, play_info
    for i in range(play_num):
        if play_info[i]["life"] == 1:
            sum(i, play_info[i]["count"])
        else:
            continue


def find_max():
    global play_num, play_info, max_point
    sum_total()
    max_point = 0
    for i in range(play_num):
        if play_info[i]["sum"] > max_point:
            max_point = play_info[i]["sum"]


def winner():
    global play_num, play_info
    find_max()
    for i in range(play_num):
        if play_info[i]["sum"] == max_point:
            play_info[i]["winner"] = 1


def get_is_winner(pid):
    global get
    if get == 0:
        winner()
        get += 1

    if play_info[pid]["winner"] == 1:
        return 1
    else:
        return 0


def main():
    pass

def get_max_point():
    return max_point