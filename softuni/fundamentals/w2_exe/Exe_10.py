lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmets = lost_fights // 2
broken_swords = lost_fights // 3
broken_shields = lost_fights // 6
broken_armor = broken_shields // 2

expense = helmet_price * broken_helmets + sword_price * broken_swords + shield_price * broken_shields +\
          armor_price * broken_armor

print(f"Gladiator expenses: {expense:.2f} aureus")