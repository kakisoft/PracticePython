def fib(n):    # nまでのフィボナッチ数を出力する
    """nまでのフィボナッチ数をprintする。"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# 定義した関数を呼び出す:
fib(2000)
