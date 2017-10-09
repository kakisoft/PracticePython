"""
__enter__ と __exit__ を実装したクラスは コンテキストマネージャ と呼ばれる。
with 文に入った時に __enter__ メソッドが呼ばれ、with 文を抜けるときに __exit__ メソッドが呼ばれる。
"""
class TraceContextManager:
    # 
    def __enter__(self):
        print("__enter__  called")

    def __exit__(self,exc_type, exc_value, traceback):
        print("__exit__  called")

with TraceContextManager():
    print("hello") 
#=>
# __enter__  called
# hello
# __exit__  called