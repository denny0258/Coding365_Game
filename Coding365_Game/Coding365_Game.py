# -*- coding: utf-8 -*-
# 系統啟動
# 請必須包含Model資料夾並確保有Test模塊
# 啟動之後請確保各自開發的程序無 ERROR
# ----------------------------
import sys
import os
<<<<<<< HEAD
sys.path.append(".\\Model")
# from Tests import Test
# import Central_control

print(os.getcwd())
=======
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "Coding365_Game", "Model"))
# ----------------------------
from Tests import Test
import Central_control
>>>>>>> 742e3c4ece561a551a85f27206afdd47d1dd4603


def Start():
    # Test()
    # Central_control.start()
    pass


if __name__ == "__main__":
    Start()
