#1
import math
a = int(input('Input degree: '))
print("Output radian:", math.radians(a))

#2
def trapezoid_area():    
    h = int(input("Height: "))
    a = int(input('Base, first value: '))
    b = int(input('Base, second value: '))
    print("Expected Output: ", (a+b)/2*h)
trapezoid_area()

#3
import math
def trapezoid_area():    
    s = int(input("Input number of sides: "))
    h = int(input('Input the length of a side: '))
    a = ((s*pow(h,2))/4) * math.tan(math.radians(180/s))
    print("The area of the polygon is: ", a)
trapezoid_area()

#4
def parallelogram():
    a = int(input('Length of base: '))
    h = int(input('Height of parallelogram: '))
    print('Expected Output:', float(a*h))
parallelogram()