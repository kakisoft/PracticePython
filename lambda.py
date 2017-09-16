# lambda 引数1, 引数2: 条件式
smaller1 = lambda num1, num2: num2 if num1 > num2 else num1

#↑と同一
def smaller(num1, num2):
    return num2 if num1 > num2 else num1

print(smaller(9,2))  #=> 2
print(smaller(1,11)) #=> 1

