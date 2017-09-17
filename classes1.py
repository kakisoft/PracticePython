from datetime import date

class Customer:
    bmi = 22  #クラス変数
    # 初期化メソッド（コンストラクタ）
    def __init__(self, number, name, height=0):
        self.__number = number  # 先頭に「__」を付ける事で、カプセル化できる。
        self.__name = name      # 付けない場合はパブリックアクセスできる。
        self.__height = height
        self._point = 1         # 「_」を１つだけ付けると、「外部からアクセスしてほしくない」という意味だそうな。（アクセス可）

    # getter
    def get_name(self):
        return self.__name;
    def get_number(self):
        return self.__number
    def get_height(self):
        return self.__height;

    # setter
    def set_number(self, number):
        self.__number = number

    # プロパティ
    name = property(get_name)                 # この宣言で、「get_name()」でなく、「instance.name」とコールできる。
    number = property(get_number, set_number)
    height = property(get_height)

    # メソッドを定義
    def std_weight(self):
        return Customer.bmi * (self.__height / 100) ** 2


# クラス変数にアクセス
Customer.bmi = 23
print(Customer.bmi)

# インスタンス生成
taro = Customer(101, "斎藤太郎", 180)
print("{}:{}{}cm".format(taro.get_number(), taro.name, taro.get_height()))
print("{} -> bmi:{}".format(taro.get_name(), Customer.bmi))
print("{} 標準体重:{:.2f}kg".format(taro.get_name(), taro.std_weight()))
print(taro._point)

# プロパティを変更
taro.__height = 175
print("{}:{}{}cm".format(taro.get_number(), taro.get_name(), taro.get_height()))

# インスタンスに変数を動的に追加
taro.birthdate = date(1989, 7, 3)
print("{} 誕生日:{}".format(taro.get_name(), taro.birthdate))

# クラス変数を動的に追加
Customer.LIMIT = 50
print(taro.LIMIT) #=> 50

# メソッドを動的に追加
def show_info(self):
    print("{}: {}".format(self.get_number(), self.get_name()))

Customer.show_info = show_info
hanako = Customer(102, "山田花子", 150)
hanako.show_info()
