needed_experience = float(input())
battle_count = int(input())
total_experience = 0

for battle in range(1, battle_count + 1):
    experience = float(input())

    if battle % 3 == 0:
        experience += 0.15 * experience
    if battle % 5 == 0:
        experience -= 0.10 * experience
    if battle % 15 == 0:
        experience += 0.05 * experience

    total_experience += experience

    if total_experience >= needed_experience:
        print(f"Player successfully collected his needed experience for {battle} battles.")
        break

if total_experience < needed_experience:
    needed_experience = needed_experience - total_experience
    print(f"Player was not able to collect the needed experience, {needed_experience:.2f} more needed.")
