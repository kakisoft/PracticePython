### List
height = [10, 20, 30, 40, 50]

print(height)      #⇒ [10, 20, 30, 40, 50]
print(height[-1])  #⇒ 50
print(len(height)) #⇒ 5


### Tuple
width = (11, 22, 33, 44, 55)


### シーケンス型のキャスト
tuple1 = ("A", "B", "C", "D", "E")
list1  = list(tuple1) # タプルをリストに変換
tuple2 = tuple(list1) # リストをタプルに変換
print(list1, tuple2)

## rangeオブジェクトをlistに変換可(0から開始、101で終了、10加算)
for counter in list(range(0,101,10)):
    print(counter)
else:
    print("ループが完了しました。")

# zip
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