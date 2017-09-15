colors = {"red":"赤", "blue":"青", "yello":"黄"}
print(colors)

print(colors["red"]) # ⇒ 赤
print(len(colors))   # ⇒ 3

colors["greed"] = "緑"  # 追加
del colors["red"]       # 削除

if "blue" in colors:
    print("blue ditected")
    
# キー、値の一覧を取得
print(colors.keys())   # ⇒ dict_keys(['blue', 'yello', 'greed'])
print(colors.values()) # ⇒ dict_values(['青', '黄', '緑'])
# これらは「ビュー」と呼ばれる種類のオブジェクト。リストに変換するには以下。
print(list(colors.keys()))   # ['blue', 'yello', 'greed']
print(list(colors.values())) # ['青', '黄', '緑']

# すべてのキーと値のペアを取得
print(colors.items()) # ⇒ dict_items([('blue', '青'), ('yello', '黄'), ('greed', '緑')])

# イテレート可
for jap, eng in colors.items():
    print("{}:{}".format(jap,eng))

