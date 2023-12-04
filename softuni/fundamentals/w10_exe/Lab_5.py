text = input()

nums, strings, chars = "", "", ""

for c in text:
    if c.isdigit():
        nums += c
    elif c.isalpha():
        strings += c
    else:
        chars += c

print(nums)
print(strings)
print(chars)