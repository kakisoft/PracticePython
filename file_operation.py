import random

FILE_NAME_FULL_PATH = "resources/sample1.txt"

# 基本操作
file = open(FILE_NAME_FULL_PATH, "r", encoding="utf_8")
lines = file.read()
print(lines)
file.close()

# With句を使用（close不要）
with open(FILE_NAME_FULL_PATH, "r", encoding="utf_8") as file:
    for i, line in enumerate(file):
        print("{:4d}:{}".format(i + 1, line.rstrip("\n")))


# 読み込む文字数を指定
file = open(FILE_NAME_FULL_PATH, "r", encoding="utf_8")
lines = file.read(2) #最初の2文字
print(lines)
lines = file.read(2) #次の2文字
print(lines)
file.close()

# ファイル各行をリスト分割
file = open(FILE_NAME_FULL_PATH, "r", encoding="utf_8")
lines = file.readlines()
for i, line in enumerate(lines):
    print("{:4d}:{}".format(i + 1, line), end="") #改行をカットする
   #print("{:4d}:{}".format(i + 1, line.rstrip("\n")))
print("")

# １行ずつ読み込む（ファイルオブジェクトをイテレート）
file = open(FILE_NAME_FULL_PATH, "r", encoding="utf_8")
for i, line in enumerate(file):
    print("{:4d}:{}".format(i + 1, line.rstrip("\n")))
file.close()

# １行ずつ読み込む（whileを使うパターン）
file = open(FILE_NAME_FULL_PATH, "r", encoding="utf_8")
i = 0
while True:
    line = file.readline()
    if line == "":
        break
    print("{:4d}:{}".format(i + 1, line.rstrip("\n")))
    i += 1
file.close()

