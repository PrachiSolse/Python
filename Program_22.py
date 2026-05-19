# Solution of Quadratic Equation
import math
a=float(input("Enter value of a:"))
b=float(input("Enter VAlue of b:"))
c=float(input("Enter value of c:"))

discriminant= b**2-4*a*c

if discriminant>0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Root_1:",root1)
    print("Root_2:",root2)

elif discriminant==0:
    root = -b / (2*a)
    print(f"Root: {root}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")
