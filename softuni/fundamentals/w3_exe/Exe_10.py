event = input().split("|")
coins, energy = 100, 100
open_bool = True

for i in event:
    event_items = i.split("-")
    type_event = event_items[0]  #type, amount = i.split("-")
    amount = int(event_items[1])  #amount = int(amount)

    if type_event == "rest":
        current_energy = energy
        energy += amount
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif type_event == "order":
        if energy >= 30:
            energy -= 30
            coins += amount
            print(f"You earned {amount} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        if coins >= amount:
            coins -= amount
            print(f"You bought {type_event}.")
        else:
            open_bool = False
            break

if open_bool:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
else:
    print(f"Closed! Cannot afford {type_event}.")
