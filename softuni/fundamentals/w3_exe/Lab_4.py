num = int(input())
word = input()
strings = []

for _ in range(num):
    curr_str = input()
    strings.append(curr_str)

filtered_strings = []

for i in strings:
    if word in i:
        filtered_strings.append(i)

print(strings)
print(filtered_strings)