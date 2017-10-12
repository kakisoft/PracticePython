class SpecialMethod():
    # コンストラクタ
    def __init__(self,value):
        self.value = int(value)

    #=====< 以下、演算子オーバーロード用の機能？ >=====
    
    # 加算する時にコールされる
    def __add__(self, _self):
        return SpecialMethod(self.value + _self.value)

    # intメソッドをコールする時に呼び出される
    def __int__(self):
        return 999

    # iterメソッドをコールする時に呼び出される
    def __iter__(self):
        return iter([1,2,3])

    # boolメソッドをコールする時に呼び出される
    def __bool__(self):
        return self.value <= 0

instance1 = SpecialMethod(3)
instance2 = SpecialMethod(7)

sp_result1 = instance1 + instance2
print(sp_result1.value) #=> 10
print(int(sp_result1))  #=> 999

sp_result2 = iter(SpecialMethod(9))
print(list(sp_result2))   #=> [1, 2, 3]
print(tuple(sp_result2))  #=> (1, 2, 3)
print(set(sp_result2))    #=> {1, 2, 3}

print(bool(sp_result2)) #=> True


#=========================
#      ドキュメント
#=========================
def doc_sample(message):
    """__doc__ message"""
    print(message)

print(doc_sample.__doc__) #=> __doc__ message
