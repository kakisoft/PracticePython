# lambda 引数1, 引数2, 引数3, ....: 処理　<キーワード引数を使用>
doll_to_yen = lambda doll, rate=105: doll * rate
print(doll_to_yen(doll=5)) #=> 525

# 基本パターン
smaller1 = lambda num1, num2: num2 if num1 > num2 else num1

#↑と同一
def smaller(num1, num2):
    return num2 if num1 > num2 else num1

print(smaller(9,2))  #=> 2
print(smaller(1,11)) #=> 1

# map
inches = [9, 5.5, 6, 4, 5, 6.5, 10]
cms = list(map(lambda n:n * 2.54, inches))
print(cms)

