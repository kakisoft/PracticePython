"""
可変長引数
"""
#printの例　※先頭が可変長引数で、それ以降はキーワード引数
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

print(1,2,"Hello","Python", sep="-") #=> 1-2-Hello-Python

def func1(arg1, *arg2):
    print(arg1, arg2)

def func2(*arg1, arg2):
    print(arg1, arg2)

func1(1,2,3,4) #=> 1 (2, 3, 4) ※２番目以降の引数はタプルとなる
func1("hello", "Python", 2017, 9, 16) #=> hello ('Python', 2017, 9, 16) ※２番目以降の引数はタプルとなる

func2(1,2,3,arg2=4) #=> (1, 2, 3) 4  ※先頭に可変長引数を設定した場合、以降はキーワード引数を使用する。
func2("hello", "Python", 2017, 9, arg2=16) #=> ('hello', 'Python', 2017, 9) 16 


"""
辞書を引数に渡す場合
"""
def func(arg1, **dic): # キーワード引数を使用しない場合、dictは最後尾に設定する
    print(arg1, dic)

func("d1", name="田中一郎", nu=1) #=> d1 {'name': '田中一郎', 'nu': 1}
func("d2", name="山田太郎", age=59, num=2, point=60) #=> d2 {'name': '山田太郎', 'age': 59, 'num': 2, 'point': 60}




