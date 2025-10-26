class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

match points:
    case []:
        print("座標が存在しない")
    case [Point(0, 0)]:
        print("原点")
    case [Point(x, y)]:
        print(f"1つの座標 {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Y軸の {y1}, {y2} に2つの座標")
    case _:
        print("それ以外のどこか")