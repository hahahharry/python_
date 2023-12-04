num = int(input())
numbers = []

for _ in range(num):
   curr_num = int(input())
   numbers.append(curr_num)

word = input()

filtered_numbers = []

if word == "even":
    for i in numbers:
        if i % 2 == 0:
            filtered_numbers.append(i)
elif word == "odd":
    for i in numbers:
        if i % 2 != 0:
            filtered_numbers.append(i)
elif word == "negative":
    for i in numbers:
        if i < 0:
            filtered_numbers.append(i)
elif word == "positive":
    for i in numbers:
        if i >= 0:
            filtered_numbers.append(i)

print(filtered_numbers)