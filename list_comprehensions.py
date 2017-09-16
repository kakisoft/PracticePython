"""
＜基本式＞
 [式 for 変数 in イテレート可能なオブジェクト]
"""

#基本操作
list2 = [num ** 2 for num in range(1, 21, 2)]
print(list2) # => [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]

#↑と同じ
list1 = []
for num in range(1, 21, 2):
    list1.append(num ** 2)

print(list1) # => [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]


#リストからリストを生成
dolls = [1, 5, 9.5, 100] #() と、タプルにしてもOK
rate = 101
yens = [doll * rate for doll in dolls]
print(yens) #=> [101, 505, 959.5, 10100]

#出力内容を編集
weekdays = [day + "曜日" for day in "月火水木金土日"]
print(weekdays) #=> ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']

"""
＜条件を満たす要素を抽出＞
 [式 for 変数 in イテレート可能なオブジェクト if 条件式]
"""
#基本操作
nums1 = [1, 3, 7, 10 ,9 ,15 ,20 ,30]
nums2 = [n for n in nums1 if (n % 3) == 0] #3の倍数のみを抽出
print(nums2) #=> [3, 9, 15, 30]

#指定した文字列を含む要素を取り出す
address = ["東京都千代田区","千葉県船橋市","東京都杉並区","埼玉県大宮市","東京都町田市","東京都西東京市","東京都大田区","神奈川県横浜市"]
tokyo = [town[3:] for town in address if town.startswith("東京都")]
print(tokyo) #=> ['千代田区', '杉並区', '町田市', '西東京市', '大田区']

#タプルを要素とするリストから条件に合う要素を抽出する
names = [("田中一郎","男"),("山田健太","男"),("佐藤順子","女")]
men = [n[0] for n in names if n[1]=="男"]
print(men) #=> ['田中一郎', '山田健太']

#辞書の内包表記
#  {キー:値 for 変数 in イテレート可能なオブジェクト}
colors = ["yello","pink","blue","green"]
colors_dict = {color:1 for color in colors}
print(colors_dict) #=> {'yello': 1, 'pink': 1, 'blue': 1, 'green': 1}

