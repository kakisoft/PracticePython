def trace_decorator2(func):
    def wrap(*args, **kwargs):
        try:
            print("enter2")
            return func(*args, **kwargs)
        finally:
            print("exit2")
    return wrap


@trace_decorator2
def hello1():
    print("hello2")

hello1()
#=>
# enter2
# hello2
# exit2

#========================================
#　デコレータ構文を使わない場合、こうなる。　
#========================================
def trace_decorator1(func):
    def wrap():
        print("enter1")
        func()
        print("exit1")
    return wrap

def hello():
    print("hello1")

h1 = trace_decorator1(hello)
h1()
#=>
# enter1
# hello1
# exit1


