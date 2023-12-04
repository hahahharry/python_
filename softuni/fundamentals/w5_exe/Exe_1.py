seq_1 = input().split(", ")
seq_2 = input().split(", ")

substrings = []

for str_1 in seq_1:
    for str_2 in seq_2:
        if str_1 in str_2:
            substrings.append(str_1)
            break
print(substrings)