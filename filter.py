inches = [9, 5.5, 6, 4, 5, 6.5, 10]

def larger_5(inch):
    return inch > 5

cmsA = []
for inch in filter(larger_5, inches):  #map(関数,リスト)　処理結果は「マップオブジェクト」という、イテレート可能なオブジェクト。
    cmsA.append(inch * 2.54)
print(cmsA) #=> [22.86, 13.97, 15.24, 16.51, 25.4]

# ラムダ式を使用する場合
cmsB = []
for inch in filter(lambda inch:inch > 5, inches):
    cmsB.append(inch * 2.54)
print(cmsB) #=> [22.86, 13.97, 15.24, 16.51, 25.4]

# リスト内包表記を使用する場合
cms3 = [inch * 2.54 for inch in inches if inch > 5]
print(cms3) #=> [22.86, 13.97, 15.24, 16.51, 25.4]