import random

# 乱数
kuji = ["大吉","中吉","凶"]
print(kuji[random.randrange(len(kuji))])  # リストからランダムに出力
print(random.randint(1, 10))              # 1～10の中からランダムに出力

