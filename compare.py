### if/elif/else
num1 = 100
num2 = 3
num3 = 8

if num1 <= 10:
    print("aaaa")
elif num1 == 50:
    print("bbb")
else:
    if (num2 < 5) or (num2 > 10):
        print("out of range")
    if 1 <= num3 <= 10:
        print("1～10")
    
# ３項演算子
age = 15
msg = "未成年" if age < 20 else "成人"

# その他演算子
comp1 = [1,2,3]
comp2 = [1,2,3]

if 1 in comp1:
    print("1 in")

if 9 not in comp1:
    print("9 not in")

print(comp1 == comp2) # True：同値のため
print(comp1 is comp2) # False：同一オブジェクトでないため
print(1 is not 1.0)   # true：同一オブジェクトでないため

### 比較
comp3 = (5, 1)
comp4 = (1, 2, 3, 4, 5)
print(comp3 > comp4) # 先頭の要素で判定

if [1,2,3] != [1,2,4]:
    print("一つでも異なる要素があるとFalse")

