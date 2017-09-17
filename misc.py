import random
FILE_NAME_FULL_PATH_1 = "resources/sample1.txt"
FILE_NAME_FULL_PATH_2 = "resources/sample2.txt"

#------------------------------------------
# 平均(ラムダ式)
#------------------------------------------
average = lambda *nums: sum(nums) / len(nums)
print(average(1,2,3,4,5,6)) #=> 3.5

#------------------------------------------
# 平均
#------------------------------------------
def average(*nums):
    return sum(nums) / len(nums)    

#------------------------------------------
# 乱数
#------------------------------------------
def random_number():
    kuji = ["大吉","中吉","凶"]
    print(kuji[random.randrange(len(kuji))])  # リストからランダムに出力
    print(random.randint(1, 10))              # 1～10の中からランダムに出力


#------------------------------------------
# 読み込んだファイルをランダムに１行表示
#------------------------------------------
def random_read_line():
    file = open(FILE_NAME_FULL_PATH_1, "r", encoding="utf_8")
    lines = file.readlines()
    phrase = lines[random.randrange(len(lines))]
    print(phrase.rstrip("\n"))

#------------------------------------------
# アンケート１
#------------------------------------------
def questionnaire1():
    questionnaire = ["非常に良い","良い","普通","悪い","非常に良い"
                ,"良い","良い","普通","良い","悪い"
                ,"非常に良い","非常に悪い","普通","普通","良い"]
    results = {}
    for answer in questionnaire:
        if answer in results:
            results[answer] += 1
        else:
            results[answer] = 1

    for answer, num in results.items():
        print("<result1> {}:{}".format(answer, num))

    #得標が多い順にソート
    for answer in sorted(results.items(), key=lambda c:c[1], reverse=True):
        print("<result2> {}:{}".format(answer[0], answer[1]))

    # 非常に良い:3
    # 良い:5
    # 普通:4
    # 悪い:2
    # 非常に悪い:1

#------------------------------------------
# アンケート２（テキストファイルから読み込み）
#------------------------------------------
def questionnaire2():
    results = {}
    with open(FILE_NAME_FULL_PATH_2, "r", encoding="utf_8") as file:
        for line in file:
            answer = line.rstrip("\n")
            if answer in results:
                results[answer] += 1
            else:
                results[answer] = 1
    #結果をソートして表示
    for answer in sorted(results.items(), key=lambda c:c[1], reverse=True):
        print("<result3>","{}:{}".format(answer[0], answer[1]))


print(average(1,2,3,4,5)) #=> 3.0
random_number()
random_read_line()
questionnaire1()
questionnaire2()
