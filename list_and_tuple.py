"""
### List
"""
height = [10, 20, 30, 40, 50]

# 基本操作
print(height)      #⇒ [10, 20, 30, 40, 50]
print(height[-1])  #⇒ 50
print(len(height)) #⇒ 5

# スライス
print(height[1:3]) # [20, 30]（リスト[開始位置:終了位置]）
print(height[:3])  # [10, 20, 30]
print(height[2:])  # [30, 40, 50]
print(height[::2]) # [10, 30, 50]（:ステップ数）

# 要素を操作
height[0] = 99             # index指定
height.append(88)          # 末尾に追加
height.append([11,22,33])  # 末尾に追加
print(height) # [99, 20, 30, 40, 50, 88, [11, 22, 33]]
print(height[6][2]) # ⇒33
height.remove(99)          # リストから要素の中から99を削除
del height[5]              # indexを指定して削除
del height[0:2]            # indexを指定して削除(スライス)
height.reverse()           # リバース
print(max(height))         # 最大値
print(min(height))         # 最小値
print(sum(height))         # 合計
height.sort(reverse=True)  # 降順(省略時はこれ。)
height.sort(reverse=False) # 昇順
so_list = sorted(height)   # 整列したリストを生成（昇順）

# 検索１
if 50 in height:
    print("50は含まれている")

# 検索２
print(height.index(50)) # 4（インデックスを返す。）

# 結合
list1 = ["春","夏"]
list2 = ["秋","冬"]
joined_list = list1 + list2
print(joined_list) # ['春', '夏', '秋', '冬']

# 繰り返し
list3 = ["山"] * 4
print(list3) # ['山', '山', '山', '山']

## rangeオブジェクトをlistに変換可(0から開始、101で終了、10加算)
for counter in list(range(0,101,10)):
    print(counter)
else:
    print("ループが完了しました。")

"""
### Tuple
"""
width = (11, 22, 33, 44, 55)

### シーケンス型のキャスト
tuple1 = ("A", "B", "C", "D", "E")
list1  = list(tuple1) # タプルをリストに変換
tuple2 = tuple(list1) # リストをタプルに変換
print(list1, tuple2)

"""
# zip
"""
weekday1 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
weekday2 = ["日" ,"月" ,"火" ,"水" ,"木" ,"金" ,"土"]
for(eng, jap) in zip(weekday1, weekday2): #どちらかの要素がなくなったらroop終了
    print(eng , ":", jap)
    if eng == "Fri":
        print("ループを中断しました。")
        break
else:
    print("breakを実行する場合、ここは実行されない。")

# zip2
str1 = "SMTWTFS"
str2 = "uouehra"
str3 = "nneduit"
for(w1,w2,w3) in zip(str1, str2, str3):
    print(w1 + w2 + w3) # Sum, Mon, Tue...
