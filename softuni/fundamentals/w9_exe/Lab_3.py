stock = {}

while True:
    cmd = input()
    if cmd == "statistics":
        break
    else:
        product, quantity = cmd.split(': ')
        quantity = int(quantity)

        if product in stock:
            stock[product] += quantity
        else:
            stock[product] = quantity

product_counter = len(stock.keys())
quantity_total = sum(stock.values())

print("Products in stock:")

for product, quantity in stock.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {product_counter}")
print(f"Total Quantity: {quantity_total}")