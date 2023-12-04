days = int(input())
plunder_day = int(input())
expected_plunder = int(input())

total_plunder = 0

for i in range(1, days + 1):
    total_plunder += plunder_day

    if i % 3 == 0:
        total_plunder += 0.5 * plunder_day

    if i % 5 == 0:
        total_plunder -= 0.3 * total_plunder

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {100 * total_plunder/expected_plunder:.2f}% of the plunder.")