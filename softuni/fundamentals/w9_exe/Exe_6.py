inventory = {}
inventory_prices = {}
final_inventory = {}

while True:
    cmd = input()

    if cmd == "buy":
        break

    product, price, qty = cmd.split()
    price = float(price)
    qty = int(qty)

    if product not in inventory.keys():
        inventory[product] = 0
    inventory[product] += qty
    inventory_prices[product] = price
    final_inventory[product] = inventory[product] * inventory_prices[product]

for k, v in final_inventory.items():
    print(f"{k} -> {v :.2f}")





