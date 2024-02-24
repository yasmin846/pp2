#1
def generate_square(n):
    for i in range(n+1):
        yield i**2
for i in generate_square(int(input())):
    print(i)

#2
def generate_even(n):
    for i in range(n+1):
        if i%2 == 0:
            yield i
        else:
            yield ','
for i in generate_even(int(input())):
    print(i, end = '')

#3
def generate_34(n):
    for i in range(n+1):
        if i%3 == 0 and i%4 == 0:
            yield i
for i in generate_34(int(input())):
    print(i)

#4
def square(n, b):
    for i in range(n, b+1):
        yield i**2
for i in square(int(input()), int(input())):
    print(i)

#5
def down(n):
    for i in range(n+1):
        while n>i:
            yield n
            n -=1
for i in down(int(input())):
    print(i)