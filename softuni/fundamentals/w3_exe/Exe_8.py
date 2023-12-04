# Step 1: Parse the input
fires_info = input().split("#")
water = int(input())

# Step 2: Initialize variables to track results
total_effort = 0
cells_put_out = []

# Step 3: Process each fire cell
for fire in fires_info:
    fire_type, value = fire.split(" = ")
    value = int(value)

    if fire_type == "High" and 81 <= value <= 125:
        if water >= value:
            water -= value
            total_effort += 0.25 * value
            cells_put_out.append(value)
    elif fire_type == "Medium" and 51 <= value <= 80:
        if water >= value:
            water -= value
            total_effort += 0.25 * value
            cells_put_out.append(value)
    elif fire_type == "Low" and 1 <= value <= 50:
        if water >= value:
            water -= value
            total_effort += 0.25 * value
            cells_put_out.append(value)

# Step 4: Print the results
print("Cells:")
for cell in cells_put_out:
    print(f" - {cell}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(cells_put_out)}")
