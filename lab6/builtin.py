import time, math
#1

#2
here = input()
upp = 0
low = 0
for i in range(len(here)) :
    if here[i] >= 'a' and here[i] <= 'z' :
        low += 1
    else:
        upp += 1
print(f"Uppercase letters: {upp} \nLowercase letters: {low}")

#3
str1 = input()
if (str1 == str1[::-1]):
    print("TRUE")
else:
    print("FALSE")

#4
def root(milsec, n):
    time.sleep(milsec/1000)
    return math.sqrt(n)
n = int(input("Sample Input:\n"))
milsec = int(input())
print("Sample Output:")
print(f"Square root of {n} after {milsec} is {root(n, milsec)}")

#5
hey = (True, True, True, False)
print(all(hey))