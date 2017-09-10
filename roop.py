list1 = [1,2,3,4,5]

wcnt = 0
while wcnt < 5:
    wcnt += 1

# リスト
for num in list1:
    print(num)

# renge(1～9)
for counter in range(10):
    print(counter)

# renge(1～104) 　
for counter in range(100, 105):
    print(counter)

# 3から30までの3の倍数を表示
for counter in range(3, 31, 3):
    print(counter)

# 10から開始し、デクリメント。最終出力値は 0(カウンタが-1になったら終了)
for counter in range(10, -1, -1):
    if counter == 3:
        break     #ループ終了
    if counter > 7:
        continue  #ループの先頭に戻る
    print(counter)

# enumrate
countries = ["フランス","アメリカ","中国","ドイツ","日本"]
for index, country in enumerate(countries):
    print(str(index +1) + ":" , country)

