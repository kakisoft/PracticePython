class SpecialMethod():
    # コンストラクタ
    def __init__(self,value):
        self.value = int(value)

    #====================================
    # 以下、演算子オーバーロード用の機能？
    #====================================
    
    # 加算する時にコールされる
    def __add__(self, _self):
        return SpecialMethod(self.value + _self.value)

    # intメソッドをコールする時に呼び出される
    def __int__(self):
        return 999

instance1 = SpecialMethod(3)
instance2 = SpecialMethod(7)

sp_result1 = instance1 + instance2
print(sp_result1.value) #=> 10
print(int(sp_result1))  #=> 999


