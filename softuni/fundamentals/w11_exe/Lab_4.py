import re

text = input()
validation = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
result = re.finditer(validation, text)

for i in result:
    print(i.group(), end=" ")


