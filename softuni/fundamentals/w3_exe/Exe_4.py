string = input().split(", ")
count = int(input())
collected_coins = []

for i in string:
    collected_coins.append(int(i))

final_sum = []
index = 0

while index < count:
    current_sum = 0

    for current_index in range(index, len(collected_coins), count):
        current_sum += collected_coins[current_index]
    final_sum.append(current_sum)
    index += 1

print(final_sum)