number = int(input())
highest_value = 0
h_quality = 0
h_weight = 0
h_time = 0

for _ in range(number):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    curr_value = (weight / time_needed) ** quality

    if curr_value > highest_value:
        highest_value = curr_value
        h_weight = weight
        h_time = time_needed
        h_quality = quality

print(f"{h_weight} : {h_time} = {highest_value:.0f} ({h_quality})")
