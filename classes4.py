"""
組み込み型の拡張
"""
class NumList(list):
    # 正の値を合計
    def sum_plus_value(self):
        sum = 0
        for n in self:
            if n > 0:
                sum += n
        return sum

    # 負の値を0に設定
    def remove_minus_value(self):
        sum = 0
        for i in range(len(self)):
            if self[i] < 0:
                self[i] = 0

if __name__ == "__main__":
    list1 = NumList([1, 2, 3, -4, 9, -9])
    list1[1] = 4
    print("合計:{}".format(list1.sum_plus_value()))
    list1.remove_minus_value()
    print(list1)