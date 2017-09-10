import calendar, math
from math import sqrt, pow

cal = calendar.TextCalendar(0)  # [0:月, 1:火, 2:水, 3:木, 4:金, 5:土, 6:日] から開始
cal.prmonth(2017, 8)

print(math.sqrt(16))  # 平方根
print(math.pi)        # 円周率

print(sqrt(25))    # from区を指定すると、mathを省略可
print(pow(2, 3))   # 2の3乗

