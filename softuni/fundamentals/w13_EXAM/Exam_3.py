heroes = {}

while True:
    cmd = input().split()
    if cmd[0] == "End":
        break

    if cmd[0] == "Enroll":
        hero_name = cmd[1]
        if hero_name not in heroes:
            heroes[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")

    elif cmd[0] == "Learn":
        hero_name = cmd[1]
        spell_name = cmd[2]
        if hero_name in heroes:
            if spell_name not in heroes[hero_name]:
                heroes[hero_name].append(spell_name)
            else:
                print(f"{hero_name} has already learnt {spell_name}.")
        else:
            print(f"{hero_name} doesn't exist.")

    elif cmd[0] == "Unlearn":
        hero_name = cmd[1]
        spell_name = cmd[2]
        if hero_name in heroes:
            if spell_name in heroes[hero_name]:
                heroes[hero_name].remove(spell_name)
            else:
                print(f"{hero_name} doesn't know {spell_name}.")
        else:
            print(f"{hero_name} doesn't exist.")

print("Heroes:")
for hero, spells in heroes.items():
    print(f"== {hero}: {', '.join(spells)}")
