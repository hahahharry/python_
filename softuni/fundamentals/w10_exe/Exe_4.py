text = input()
new_text = ""

for i in text:
    char = ord(i)+3
    f_char = chr(char)
    new_text += f_char

print(new_text)