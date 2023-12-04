import re

purchases = {}
total_cost = 0

while True:
    line = input()
    if line == "Purchase":
        break

    match = re.match(r">>([A-Za-z\s]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)", line)

    if match:
        furniture_name = match.group(1)
        price = float(match.group('price'))
        quantity = int(match.group('quantity'))

        total_cost += price * quantity

        if furniture_name not in purchases:
            purchases[furniture_name] = 0
        purchases[furniture_name] += price * quantity

print("Bought furniture:")
for furniture in purchases:
    print(f"{furniture}")
print(f"Total money spend: {total_cost:.2f}")