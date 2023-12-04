num_1 = int(input())
num_2 = int(input())

numbers = []

while num_2 > 0:
    for i in range(num_1, num_1 * num_2 + 1):
        if i % num_1 == 0:
            numbers.append(i)
            num_2 -= 1


print(numbers)