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


# 外部から参照される場合、コールされない。
if __name__ == "__main__":
    hanako = Customer(102, "山田花子", 179)
    print("{} 標準体重:{:.2f}kg".format(hanako.name, hanako.std_weight()))
