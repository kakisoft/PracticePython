"""
宣言
"""
value1 = 10

#基本
def doll_to_yen1(doll, rate):
    yen = doll * rate   #ローカルスコープ
    global value1 = 100 #グローバル変数にアタッチする場合
    print("為替レート:{}".format(rate))
    print("{}ドルは{}円".format(doll,yen))
    return yen

#デフォルト値を設定
def doll_to_yen2(doll, rate=100):
    yen = doll * rate
    print("為替レート:{}".format(rate))
    print("{}ドルは{}円".format(doll,yen))

#ミュータブルなオブジェクトを引数に渡す
def mmu_test(list1):
    print("list1:{}".format(id(list1)))
    list1[0] = 0
    list1.append(100)
    print("list1:{}".format(id(list1)))

"""
使い方
"""
rate = 100
doll = 105

#基本
yen = doll_to_yen1(doll, rate)

#キーワード引数
yen = doll_to_yen1(rate=110, doll=200)

#デフォルト引数
yen = doll_to_yen2(200, 120)
yen = doll_to_yen2(200)

#ミュータブルなオブジェクトを引数に渡す
list2 = [1,2,3]
mmu_test(list2)
print(list2)    #=> [0, 2, 3, 100]


