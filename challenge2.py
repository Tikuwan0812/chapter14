class Square:
    def __init__(self, side):
        self.side = side
    
    def __repr__(self):
        return "{0} by {0} by {0} by {0}".format(self.side)

a_square = Square(29)
print(a_square)