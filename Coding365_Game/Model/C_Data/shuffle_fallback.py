import random

poker = []
for i in range(52):
    poker.append({"num": 0, "color": 0})


suit = 0
number = 0


def init(poker):
    index = 0
    for i in range(1, 5):
        for j in range(1, 14):
            poker[index]["color"] = i
            poker[index]["num"] = j
            index += 1


def shuffle(poker, len):
    i = len
    while i > 0:
        j = random.randint(0, 9999) % i
        i -= 1
        temp = poker[i]
        poker[i] = poker[j]
        poker[j] = temp


index = 0

def do_shuffle():
    global index, poker
    index = 0
    shuffle(poker, 52)


def do_next():
    global suit, number, index

    if index == 52:
        return 0
    suit = poker[index]["color"]
    number = poker[index]["num"]
    index+=1
    return 1


def do_init():
    global poker
    init(poker)

def main():
    return 0



do_init()

def Take_Card(shuffle):
    if shuffle:
        do_shuffle()
    
    if do_next() == 1:
        return ("shdc"[suit-1], number)
    return None

