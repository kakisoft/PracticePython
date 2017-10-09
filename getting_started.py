"""
複数行コメント
"""
pass
print("What's Going ON")
print(2017, 9, 6)
print(str(2017) + "年")

# xを20回表示
print('x' * 20)  

# 出力後に改行しない
print("Hello", "-", end="") 
print("World") 

# Class Check
print(type(3))    #<class 'int'>
print(type(3.14)) #<class 'float'>
print(type("3"))  #<class 'str'>

# Cast1
print(type(float(1))) #<class 'float'>
print(type(int("3"))) #<class 'int'>

# conversion1
num1 = int("FFF", 16) #「FFF」を16進数としてintに変換
num2 = int("1010", 2) #「1010」を2進数としてintに変換
print(num1,num2)

# conversion2
num3 = hex(255) # 255を16進数の文字列に変換
num4 = oct(18)  # 18を8進数の文字列に変換
num5 = bin(15)  # 15を2進数の文字列に変換
print(num3, num4, num5)

# Text Sequence
str1 = "こんにちは"
print(str1[1], str1[-1])

# id
n1 = 10
print(id(n1)) # 数値や文字列は、イミュータブルなオブジェクト
n1 = n1 + 5
print(id(n1)) # ↑と異なる結果を返す

# 複数の変数を同時にセット
m, n = 5, 10
print(m, n) #=> 5 10
