class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y


## 例
points = Point(3, 3)
# points = Point(3, 2)
# points = 0
# points = [Point(1,1), Point(2,2)]


match points:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"対角線上ではない")
    case (Point(x1, y1), Point(x2, y2) as p2):
        print(f"2点: ({x1},{y1}) と ({p2.x},{p2.y})")
    case _:
        print("それ以外のどこか")
