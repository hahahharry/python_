text = input()
f_text = ""
expl_num = 0

for index in range(len(text)):
    if text[index] != ">" and expl_num > 0:
      expl_num -= 1
    elif text[index] == ">":
        f_text += text[index]
        expl_num += int(text[index + 1])
    else:
        f_text += text[index]

print(f_text)