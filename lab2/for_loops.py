#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#2 - When the item value is "banana", jump directly to the next item.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#3 - Use the range function to loop through a code set 6 times.
for x in range(6):
    print(x)

#4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)