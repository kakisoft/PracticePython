"""
map
  リストの要素に、関数で指定した処理を行い、イテレート可能なオブジェクトを返す
"""
inches = [9, 5.5, 6, 4, 5, 6.5, 10]

def to_cm(inch):
    return inch * 2.54

inches = [9, 5.5, 6, 4, 5, 6.5, 10]
for cm in map(to_cm, inches):  #map(関数,リスト)　処理結果は「マップオブジェクト」という、イテレート可能なオブジェクト。
    print(cm)

# ラムダ式を使用する場合
cms1 = list(map(lambda n:n * 2.54, inches))
print(cms1) #=> [22.86, 13.97, 15.24, 10.16, 12.7, 16.51, 25.4]

# リスト内包表記を使用する場合
cms2  = [n * 2.54 for n in inches]
print(cms2) #=> [22.86, 13.97, 15.24, 10.16, 12.7, 16.51, 25.4]

"""
filter
   
"""
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