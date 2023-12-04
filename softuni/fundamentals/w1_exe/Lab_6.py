budget = int(input())

initial_price = 0

while True:
    command = input()

    if command == "End":
        print('You bought everything needed.')
        break

    price = float(command)

    if initial_price + price > budget:
        print('You went in overdraft!')
        break

    initial_price += price