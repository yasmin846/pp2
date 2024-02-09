#1
def function(s):
    print(28.3495231 * s)
function(int(input()))

#2
def funct(F):
    print((5/9) * (F-32))
function(int(input()))

#3
numHead = int(input())
numLeg = int(input())
def solve(numLeg, numHead):
    for numChick in range(numHead+1):
        numRabbit = numHead - numChick
        if(2*numChick + 4*numRabbit) == numLeg:
            return numChick, numRabbit
result = solve(numLeg, numHead)
print(result)

#4
def prime(num):
    for i in range(2, int(num ** 0.5)+1):
        if num%i == 0:
            return False
    return True
def filter_prime(number):
    return [num for num in number if prime(num)]
print(filter_prime([1, 4, 7, 2, 9, 45, 33, 5]))

#5
from itertools import permutations
def func(s):
    a = list(permutations(s))
    for i in a:
        print(i)
func(input())

#6
b = str(input())
def reverse(string):
    a = string.split()
    a.reverse()
    res = ''
    for i in a:
        res+= i + ' '
    return res
ans = reverse(b)
print(ans)

#7
def has_33(num):
    cnt = 0
    for i in num:
        if(i == 3):
            cnt += 1
        else:
            cnt = 0
        if(cnt>=2):
            return True
    return False
print(has_33([1, 3, 3]))    
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3])) 

#8
def spy_game(nums):
    a = ""
    for i in range(len(nums)):
        if nums[i] == 0 or nums[i] == 7:
            a = a + str(nums[i])
        else:
            continue
    if "007" in a:
        return True
    else:
        return False
nums = list(map(int, input().split()))
print(spy_game(nums))

#9
r = float(input())
def volume(r):
    return(4/3 * 3.14 * pow(r,3))
print(volume(r))

#10
def unique(list):
    uniquelist = []
    for i in list:
        if i not in uniquelist:
            uniquelist.append(i)
    return uniquelist
frst = input()
scnd= [int(x) for x in frst.split()]
print(unique(scnd))

#11
def palindrome(str):
    if(str == str[::-1]):
        return True
    else:
        return False
print(palindrome(input()))

#12
def histogram(a):
    for i in a:
        print('*' * i)
values = [4, 9, 7]
histogram(values)
'''
frst = input()
scnd= [int(x) for x in frst.split()]
'''

#13
import random
def game():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    num = random.randint(1, 20)
    a = int(input("Take a guess.\n"))
    cnt = 0
    while True:
        cnt+=1
        if a<num:
            print("Your guess is too low")
        elif a>num:
            print("Your guess is too much")
        else:
            print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
            break
        a = int(input("Take a guess.\n"))
game()