"""
＜継承＞
class サブクラス名(スーパークラス名):
    クラス本体
"""
from classes2_1 import Customer
from datetime import date

class GoldCustomer(Customer):
    def __init__(self, number, name, height=0, birthdate=0):
        self.__birthdate = birthdate
        super().__init__(number, name, height)

    # プロパティ
    def get_birthdate(self):
        return self.__birthdate
    birthdate = property(get_birthdate)

    # サブクラスにてメソッドを追加
    def get_age(self):
        now = date.today()
        age = now.year - self.birthdate.year
        if (now.month, now.day) >= (self.birthdate.month, self.birthdate.day):
            return age
        else:
            return age - 1

if __name__ == "__main__":
    taro = GoldCustomer(101, "斎藤太郎", 180, date(1978, 9, 1))
    # スーパークラスのプロパティ
    name = taro.name
    number = taro.number
    height = taro.height
    # スーパークラスのメソッド
    std_weight = taro.std_weight()
    # サブクラスのプロパティ
    birth = taro.birthdate
    # サブクラスのメソッド
    age = taro.get_age()

    print("{} {} 身長:{}cm 標準体重:{:.2f}kg 誕生日: {}".format(number, name, height, std_weight, birth))
    print("年齢:{}".format(age))
