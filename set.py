signal = {"赤","青","黄","黄","黄"}

print(signal) # => {'青', '黄', '赤'} ※重複しない

# イテレート
for s in signal:
    print(s)

#リストから集合を作成
listA = [1,2,3,3,3]
setA = set(listA)
print(setA) # => {1, 2, 3}

#基本操作
colors = {"red","green","blue"}
colors.add("orange") # 追加
colors.remove("red") # 削除
colors.clear()       # 全て削除
print(colors)

#判定
if "sun" in {"sun","moon","earth"}:
    print("true")


#演算
set1 = {"空","海","川","地球"}
set2 = {"山","海","空","空気"}
print(set1 | set2) #set1とset2のどちらかに存在する集合を作成     => {'空', '地球', '海', '空気', '川', '山'}
print(set1 & set2) #set1とset2に共通して存在する集合を作成       => {'海', '空'}
print(set1 - set2) #set1に存在し、set2に含まれない集合を作成     => {'川', '地球'}
print(set1 ^ set2) #set1とset2のどちらかにのみ存在する集合を作成 => {'空気', '川', '地球', '山'}

#リスト内包表記
# {式 for 変数 in イテレート可能なオブジェクト}
lst = [100,200,100,200,300,400,90,100,50]
num = {num for num in lst if num > 100}
print(num) #=> {200, 300, 400}

