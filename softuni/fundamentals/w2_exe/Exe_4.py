number_of_chars = int(input())
total_sum = 0

for _ in range(number_of_chars):
    char = input()
    asc_char = ord(char)
    total_sum += asc_char

print(f"The sum equals: {total_sum}")