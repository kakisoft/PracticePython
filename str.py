str1 = "Hello"

print(str1.upper())          # HELLO
print("Python".upper())      # PYTHON
print(str1.lower())          # hello
print(str1.replace("H","n")) # nello

# Contain
if str1.find("el") != -1:
    print("elを含む") # 最初にマッチするindexを返す
else:
    print("含まない")

# Contain(後ろから検索)
print(str1.rfind("el"))

# 先頭の一致
if str1.startswith("He"):
    print("先頭がHe")

# 末尾の一致
if str1.endswith("lo"):
    print("末尾がlo")

# スライス(開始位置:終了位置)
print(str1[1:3]) # el
print("月火水木金土日"[:3]) # 月火水（開始位置を省略）
print("月火水木金土日"[3:]) # 木金土日（終了位置を省略）


# 連結(イテレート可能なオブジェクト)
list1 = ["1","2","3"] 
print("-".join(list1))

# 分割
str2 = "a,b,c,d"
list2 = str2.split(",")
print(list2)

# 右から１回だけ分割
print("/path/to/foo/bar/hoge.txt".rsplit("/", 1)) # ['/path/to/foo/bar', 'hoge.txt'](os.path.split(path)使った方がいいけど。)

# カウント
print(str1.count("l"))

# ループで１文字ずつ
str3 = "春夏秋冬"
for char in str3:
    print(char) # 春、夏、秋、冬

#if 'fuga' in 'hogehoge':
