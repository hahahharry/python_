number = int(input())
total_vol_filled = 0
tank_volume = 255

for i in range(number):
    flow = int(input())

    if flow > tank_volume:
        print("Insufficient capacity!")
        continue
    tank_volume -= flow
    total_vol_filled += flow


print(total_vol_filled)