items = {"shards": 0, "fragments": 0, "motes": 0}
qty_reached = False

current_items = input().split()

while not qty_reached:
    for i in range(0, len(current_items), 2):
        value = int(current_items[i])
        key = current_items[i+1].lower()

        if key not in items.keys():
            items[key] = 0
        items[key] += value

        if items["shards"] >= 250:
            print(f"Shadowmourne obtained!")
            qty_reached = True
            items["shards"] -= 250
        elif items["fragments"] >= 250:
            print(f"Valanyr obtained!")
            qty_reached = True
            items["fragments"] -= 250
        elif items["motes"] >= 250:
            print(f"Dragonwrath obtained!")
            qty_reached = True
            items["motes"] -= 250
        if qty_reached:
            break
    if qty_reached:
        break
    current_items = input().split()

for k, v in items.items():
    print(f"{k}: {v}")

