import os, string
#1
path = os.getcwd()
print(f"Files: {[f for f in os.listdir(path) if os.path.isfile(f)]}, directories: {[d for d in os.listdir(path) if os.path.isdir(d)]} all elements are: {os.listdir(path)}")

#3
here=r'C:\Users\ExpertBook\Desktop\uni\pp2\lab6\ex.txt'
if os.path.exists(here):
    print(os.path.basename(here))
    print(os.path.dirname(here))

#4
with open(r"C:\Users\ExpertBook\Desktop\uni\pp2\lab6\ex.txt") as path:
    lines = len(path.readlines())
print(lines) 

#5
list = str(input().split())
with open(r'C:\Users\ExpertBook\Desktop\uni\pp2\lab6\ex.txt', 'w') as here:
    here.write(list)

#6
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as here:
       here.writelines(letter)

#7
with open('ex.txt', 'r') as first:
    with open('ex1.txt', 'w') as here:
        for line in first:
            here.write(line)

#8
if os.path.exists("ex1.txt"):
    os.remove("ex.txt")
else:
    print("No file")