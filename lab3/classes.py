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
class rectangle(shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)
shape = shape()
len = int(input())
wdth = int(input())
rec = rectangle(len, wdth)
rec.area()

#4
class Account():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, money):
        if money>0:
            self.balance += money
            print("Your balance: ", self.balance)
        else:
            pass
    def withdraw(self, draw):
        self.balance -= draw
        print("Your balance: ", self.balance)
account = Account("John", 10500)
print("Summ of transition:")
d = int(input())
account.deposit(d)
print("Pay the draw:")
w = int(input())
account.withdraw(w)

#5
