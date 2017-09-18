colors = {"red":"赤", "blue":"青", "yello":"黄"}
print(colors)

print(colors["red"]) #=> 赤
print(len(colors))   #=> 3
print(colors.get("purple", "登録がありません")) #keyが辞書にあれば対応する値を、無ければdefaultを返す。 

colors["greed"] = "緑"  # 追加
del colors["red"]       # 削除

if "blue" in colors:
    print("blue ditected")
    
# キー、値の一覧を取得
print(colors.keys())   #=> dict_keys(['blue', 'yello', 'greed'])
print(colors.values()) #=> dict_values(['青', '黄', '緑'])
# これらは「ビュー」と呼ばれる種類のオブジェクト。リストに変換するには以下。
print(list(colors.keys()))   # ['blue', 'yello', 'greed']
print(list(colors.values())) # ['青', '黄', '緑']

# すべてのキーと値のペアを取得
print(colors.items()) #=> dict_items([('blue', '青'), ('yello', '黄'), ('greed', '緑')])

# イテレート可
for jap, eng in colors.items():
    print("{}:{}".format(jap,eng))

#２つのリストから辞書を作成
e_seasons = ["Spring","Summer","Autumn","Winter"]
j_seasons = ["春","夏","秋","冬"]
seasons1 = {e:j for (e,j) in zip(e_seasons, j_seasons)}
print(seasons1) #=> {'Spring': '春', 'Summer': '夏', 'Autumn': '秋', 'Winter': '冬'}

#辞書のキーと値を入れ替える
seasons2 = {j:e for (e,j) in seasons1.items() }
print(seasons2) #=> {'春': 'Spring', '夏': 'Summer', '秋': 'Autumn', '冬': 'Winter'}

#リストからのキャスト
fruits_list = [["apple", "リンゴ"],['orange', "オレンジ"],['grape', "ぶどう"]]
fruits_dict = dict(fruits_list)
print(fruits_dict) #=> {'apple': 'リンゴ', 'orange': 'オレンジ', 'grape': 'ぶどう'}

#よくわからないキャスト。
direction = dict(East="東", West="西", South="南", North="北")
print(direction) #=> {'East': '東', 'West': '西', 'South': '南', 'North': '北'}


