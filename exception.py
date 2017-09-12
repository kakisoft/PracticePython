import sys

try:
    score = int("ああ")
except ValueError:
    print("Value Error")
    sys.exit()
else:
    print("例外が発生しなかった時に実行される")


print("exit() すると、ここは実行されません。")


