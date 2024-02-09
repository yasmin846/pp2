#1
class string:
    def __init__(self):
        self.string = ''
    def getString(self):
        self.string = input("Input your string: ")
    def printString(self):
        print("Uppercase: ", self.string.upper())
s = string()
s.getString()
s.printString()

#2
class shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class square(shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        print(self.length ** 2)
shape = shape()
shape.area()
square = square(int(input()))
square.area()

#3
class shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class square(shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        print(self.length ** 2)
shape = shape()
shape.area()
square = square(int(input()))
square.area()