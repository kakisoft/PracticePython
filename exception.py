import sys

try:
    score = int("ああ")
    raise ValueError    # 意図的に例外を発生させる場合
except ValueError:
    print("Value Error")
    sys.exit()
else:
    print("例外が発生しなかった時に実行される")
finally:
    print("例外の発生の有無に関係なく、必ず実行される。")


print("exit() すると、ここは実行されません。")


