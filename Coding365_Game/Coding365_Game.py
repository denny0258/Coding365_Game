# -*- coding: utf-8 -*-
# 系統啟動
# 請必須包含Model資料夾並確保有Test模塊
# 啟動之後請確保各自開發的程序無 ERROR

import sys
sys.path.append(".\\Model")
from Tests import Test
import Central_control

def Start():
    Test()
    # Central_control.start()
    pass

if __name__ == "__main__":
    Start()
