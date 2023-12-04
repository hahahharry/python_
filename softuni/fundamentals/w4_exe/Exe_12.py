import math

def factorial(a, b):
    f_1 = math.factorial(a)
    f_2 = math.factorial(b)
    return f"{f_1 / f_2:.2f}"

num1, num2 = int(input()), int(input())
print(factorial(num1, num2))

