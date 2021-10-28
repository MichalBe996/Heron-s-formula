
import math

def HeronsFormula():
    a = int(input("Enter length of first triangle side: "))
    b = int(input("Enter length of first triangle side: "))
    c = int(input("Enter length of first triangle side: "))
    perimeter = a + b + c
    s = perimeter / 2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("The area of your triangle is equal to: ", area)


while True:
    HeronsFormula()
