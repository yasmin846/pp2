#1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")

#2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#3 - Use the correct method to add multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits) 

#4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")