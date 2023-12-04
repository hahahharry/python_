num_orders = int(input())
total_price = 0

for i in range(num_orders):

    caps_price = float(input())
    if not 0.01 <= caps_price <= 100:
        continue

    days = int(input())
    if days < 1 or days > 31:
        continue

    caps_per_day = int(input())
    if caps_per_day < 1 or caps_per_day > 2000:
        continue

    single_price = caps_price*days*caps_per_day
    total_price += single_price

    print(f"The price for the coffee is: ${single_price:.2f}")

print(f"Total: ${total_price:.2f}")


