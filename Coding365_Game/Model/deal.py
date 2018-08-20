# -*- coding: utf-8 -*-

# 發牌 陳敦捷
# python c 對接 邱柏翰

try:
    from Model.C_Data import shuffle
except:
    from C_Data import shuffle


def Take_card(inputs):
    card = shuffle.Take_Card(inputs["RE"])
    return {"Card": card}


# 測試 發牌模組
# 測試項目：
# 1. 初始洗牌一次，發52張牌
#       - 確認52張牌剛好都出現一次
# 2. 52 張牌後應該顯示 None 表示沒牌
# 3. 重新洗牌後再進行一次步驟 1 確定可重複洗牌發牌
# return True: 測試通過  False: 測試失敗
def Test_inside():
    print('deal.py 發牌測試')

    for times in range(3):  # 總共進行三次測試
        re = True  # 是否需要洗牌
        cards = []  # 儲存所有牌面

        try:
            for i in range(52):
                card = Take_card({"RE": re})["Card"]
                re = False
                cards.append(card)
        except:
            print('發牌過程發生例外導致測試失敗，目前牌面陣列：')
            print(cards)
            return False

        # 計算各種花色數量
        counts = {
            "s": [0]*14,
            "h": [0]*14,
            "d": [0]*14,
            "c": [0]*14,
        }

        for card in cards:
            suit = card[0]
            number = card[1]

            if suit not in counts:
                print('牌面花色錯誤導致測試失敗:', suit)
                return False

            if number < 0 or number > 13:
                print('牌面數字範圍錯誤導致測試失敗：', number)
                return False

            counts[suit][number] += 1

        count_pass = True
        for suit in counts:
            count = counts[suit]
            for i in range(1, 13+1):
                n = count[i]
                if n != 1:
                    print('牌數量有誤：', suit, i, '數量:', n)
                    count_pass = False

        if not count_pass:
            print('牌面有誤，測試失敗')
            return False

        for i in range(5):  # 不洗牌嘗試取得5張牌
            try:
                no_card = Take_card({"RE": False})["Card"]
                if no_card is not None:
                    print('發完牌並沒有回傳 None ，測試失敗')
                    return False
            except:
                print('嘗試在發完牌後要牌發生例外，測試失敗')
                return False

        print("通過測試", times+1, "以下列出52張牌")
        print(cards)

    return True


def Test(Test_Data):
    if Test_Data.get("Hello", None) == True:
        return {"World": True}


if __name__ == "__main__":
    Test_inside()
