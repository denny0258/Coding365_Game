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

from print_API import printAPI, inputAPI


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