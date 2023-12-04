def sum_numbers(a, b):
    return a + b

def subtract(result, c):
    return result - c

def add_and_subtract(a, b, c):
    first_result = sum_numbers(a, b)
    return subtract(first_result, c)

x = int(input())
y = int(input())
z = int(input())

print(add_and_subtract(x, y, z))