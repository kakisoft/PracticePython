class Point:
    def __init__(self, x, y):
        self.x = 1
        self.y = 1

def where_is(point):
    # point は (x, y) のタプル
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")

Point(1, 1)