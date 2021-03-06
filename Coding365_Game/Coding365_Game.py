# -*- coding: utf-8 -*-
# 系統啟動
# 請必須包含Model資料夾並確保有Test模塊
# 啟動之後請確保各自開發的程序無 ERROR
# ----------------------------
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "Coding365_Game", "Model"))
# ----------------------------
from Tests import Test, Test_process
import Central_control


def Start():
    Test()
    Test_process()
    os.system("PAUSE")
    Central_control.start()
    pass


if __name__ == "__main__":
    Start()
