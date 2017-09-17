height = [10, 20, 30, 40, 50]

# 基本
height.sort(reverse=True)  # 降順(省略時はこれ。)
height.sort(reverse=False) # 昇順
so_list = sorted(height)   # 整列したリストを生成（昇順）

"""
 ソート方法のカスタマイズ
"""
list1 = ["fly","good","ABC","Bad","Woo","Foo","and"]

# 大文字、小文字を区別せずにソート
list2 = sorted(list1, key=str.upper) 
print(list2) #=> ['ABC', 'and', 'Bad', 'fly', 'Foo', 'good', 'Woo']


# ソート用の関数を定義
names1 = ["田中一郎-1979", "山田花子-2000", "井上太郎-1964", "藤本和夫-1988", "大津徹-1959", "後藤信一-1980"]
def get_year(str):
    year = str[-4:]
    return int(year)

names1.sort(key=get_year)
print(names1)


# ソートのkeyに無名関数を提議
names2 = ["田中一郎-1979", "山田花子-2000", "井上太郎-1964", "藤本和夫-1988", "大津徹-1959", "後藤信一-1980"]
names2.sort(key=lambda str:int(str[-4:]))
print(names2)

"""
 辞書の要素をソート
"""
#ラムダ式を使用
names = {"Taro":25, "Makoto":49, "Akio":30, "Kazuo":32, "Ken":48}
for name in sorted(names.items(), key=lambda n:n[0]): #n[0]の要素でソート
    print("ds1:",name[0], name[1])

#items()を引数にする（タプルの最初の値でソートする）
for name in sorted(names.items()): #結果は↑と同一
    print("ds2:",name[0], name[1])

#keys()を引数にする
for name in sorted(names.keys()): #結果は↑と同一
    print("ds3:",name, names[name])

#valueの順にソート
for name in sorted(names.items(), key=lambda n:n[1]):
    print("ds4:",name[0], name[1])

