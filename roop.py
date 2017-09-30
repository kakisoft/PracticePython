list1 = [1,2,3,4,5]

wcnt = 0
while wcnt < 5:
    wcnt += 1
    print(wcnt)  #=> 1  2  3  4  5

# リスト
for num in list1:
    print(num)  #=> 1  2  3  4  5

# renge(1～9)
for counter in range(10):
    print(counter)  #=> 0  1  2  3  4  5  6  7  8  9

# renge(100～104) 　
for counter in range(100, 105):
    print(counter)  #=> 100  101  102  103  104

# 3から30までの3の倍数を表示
for counter in range(3, 31, 3):
    print(counter)  #=> 3  6  9  12  15  18  21  24  27  30

# 10から開始し、デクリメント。最終出力値は 0(カウンタが-1になったら終了)
for counter in range(10, -1, -1):
    if counter == 3:
        break     #ループ終了
    if counter > 7:
        continue  #ループの先頭に戻る
    print(counter)  #=> 7  6  5  4

# enumrate
countries = ["フランス","アメリカ","中国","ドイツ","日本"]
for index, country in enumerate(countries):
    print(str(index +1) + ":" , country)  #=> 1: フランス  2: アメリカ  3: 中国  4: ドイツ  5: 日本  

