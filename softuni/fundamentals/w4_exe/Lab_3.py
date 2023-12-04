def calculator(operator, a: int, b: int) -> int:
    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return int(a / b)
    elif operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b

input_operation = input()
first_num = int(input())
second_num = int(input())

print(calculator(input_operation, first_num, second_num))