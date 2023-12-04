attempts = int(input())

for i in range(attempts):
    num = int(input())

    if num == 86:
        message = "How are you?"
    elif num == 88:
        message = "Hello"
    elif num > 88:
        message = "Bye."
    else:
        message = "GREAT!"

    print(f"{message}")