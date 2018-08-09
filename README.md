# Coding365_Game

Product Owner: 李汶道 (denny0258)

Scrum Master: 邱柏翰

Developers:

---

[日誌更新](https://hackmd.io/0q8J7zU3Qtqwy2L0FbjkdQ?both)

[Scrum 流程備忘](/q8XanKSMRIGnnNUTJqeeDQ)

GitHub: https://github.com/denny0258/Coding365_Game

---
### 說明
玩家需要一個基本的操作介面，來提供基本的遊玩性
- 能開始、結束遊戲
- 能看到自己有哪些牌
- 能夠決定要不要繼續拿牌，並得到新的牌
- 牌面超過21點就爆炸

---

- **中心控制系統**
    - Call 子功能、牌面紀錄、處裡玩家控制、遊戲開始結束

- **莊家發牌功能**
    - 隨機發牌

- **遊戲規則檢查系統**
    - 檢查玩家牌面超過 21 點

- **結算系統**
    - 判斷玩家輸贏

- **人數限制系統**
    - 人數限制 10 人、生成電腦玩家

- **電腦玩家**
    - 判斷拿、不拿牌，各種難度

- **籌碼系統**
    - 管理各玩家籌碼、下注 (一般玩家)、自動下注 (電腦玩家)

- **金錢系統**
    - 會計，計算玩家贏得多少籌碼

- **排行榜**
    - 紀錄遊戲結束狀態、產出排行榜
---

## function

#### Central_control 中央控制
- start 啟動程序

#### deal 莊家發牌
- Take_card 取牌
    - 傳入規格如下:

            {"RE":bool}

            bool : (True,False)
            
    - 回傳規格如下:

            {"card":(suit,number)}

            suit : (s,h,d,c)
                // s-spades黑桃h-hearts紅桃d-diamonds方塊c-clubs梅花 \\
            number : (1~13)

            回傳{"card":None}就代表沒牌了

#### monitor 遊戲規則檢
- Check_21 確認是否21點
    - 傳入規格如下:

            {
                "Player_1" : {"life":bool,"Card":list}
            }

            bool : (True,False) 
                // True = 存活
                // False = 死亡
            list : [(s,2),(h,5)]

    - 回傳規格如下:

            {
                "Player_1" : bool
            }

            bool : (True,False) 
                // True = 存活
                // False = 死亡


#### settle_accounts 勝負結算
- winner 輸出勝利者
    - 傳入規格如下:

            {
                "Player_1" : {"life":bool,"Card":list}
            }

            bool : (True,False) 
                // True = 存活
                // False = 死亡
            list : [(s,2),(h,5)]
    
    - 回傳規格如下:

            {
                "Win" : Name
            }

            Name : ("Player_1",None)


#### people 人數控制
- 限制人數不超過10人
- Get_people輸入(玩家)、(電腦) 數
    - 回傳中央規格如下:

            {
                "Player_counts" : number
            }

            number : (1~10)

    - 回傳電腦規格如下:

            {
                "computer_counts" : number
                "Difficult" : level
            }

            number : (0~9)
            level : (1~10)

#### computer_AI 電腦
- hand負責模擬玩家出牌
    - 中央傳入規格如下:

            {
                "Player_Card" : list
            }

            list : [(s,2),(h,5)]

    - 回傳規格如下:

            {
                "Get_card": bool
            }

            bool : (True,False) 

#### Chip 籌碼下注
- Get_Chip 紀錄所有玩家、電腦資料
    - 回傳規格如下:

            {
                "Player_1_Chip" : number
            }
            number : (0~9)

#### money 金錢結算
- Get_money負責所有金錢管理
    - 必須接收 winner輸出勝利者 結果
    - 回傳結果

            {
                "Player_1_money" : number 
            }
            number : (0~9)


#### Leaderboard 排行榜
- 紀錄所有資料
    - 接收 winner輸出勝利者 結果
    - 接收 money 資料
    - 接收 Get_Chip 資料
    - 回傳結果

            {
                "Player_1":{"money":number,"Chip":number,"win_rate":number,"win":number,"defeat":number}
            }