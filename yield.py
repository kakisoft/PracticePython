import random

def my_gen1(str):
    for c in str.upper():
        yield c
    
gen1 = my_gen1("Hello")
print(next(gen1)) #=> H
print(next(gen1)) #=> E
print(next(gen1)) #=> L
print(next(gen1)) #=> L
print(next(gen1)) #=> O
#print(next(gen)) #=> StopIteration(例外)

## 重複の無い乱数を返す
def random_gen(num):
    randoms = []
    while True:
        rand_num = random.randrange(num)
        #乱数に重複が無い場合
        if rand_num not in randoms:
            randoms.append(rand_num)
            yield rand_num
        #すべての乱数を生成した
        elif len(randoms) == num:
            break

rand1 = random_gen(10)
print(next(rand1))
print(next(rand1))
print(next(rand1))

#forを使用して呼び出す場合
rand2 = random_gen(100)
for r in rand2:
    print(r)

"""
ジェネレータ式
　def
"""
str2 = "Hello"
gen2 = (c for c in str2.upper())
for c in gen2:
    print(c)

#リスト内包表記にて記述
str3 = "Hello"
gen3 = [c for c in str3.upper()]
for c in gen3:
    print(c)