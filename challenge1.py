class Square:
    square_list = []

    def __init__(self, side):
        self.side = side
        self.square_list.append(self.side)

s1 = Square(10)
s2 = Square(12)
s3 = Square(20)
print(Square.square_list)