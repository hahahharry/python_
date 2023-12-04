import re

regex = "\\b_[a-zA-Z]*\\b"
text = input()

result = re.findall(regex, text)
f_list = []

for i in result:
    i = i[1:]
    f_list.append(i)

print(",".join(f_list))

