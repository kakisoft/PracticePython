import random

# 平均
def average(*nums):
    return sum(nums) / len(nums)    

# 乱数
def random_number():
    kuji = ["大吉","中吉","凶"]
    print(kuji[random.randrange(len(kuji))])  # リストからランダムに出力
    print(random.randint(1, 10))              # 1～10の中からランダムに出力

# アンケート
def questionnaire():
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
        print("{}:{}".format(answer, num))

    # 非常に良い:3
    # 良い:5
    # 普通:4
    # 悪い:2
    # 非常に悪い:1


print(average(1,2,3,4,5)) #=> 3.0
random_number()
questionnaire()