text = input()
f_text = ""
last_char = ""

for char in text:
    if char != last_char:
        f_text += char
        last_char = char

print(f_text)
