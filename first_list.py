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

