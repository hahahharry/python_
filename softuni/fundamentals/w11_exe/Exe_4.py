import re

text = input()
regex = r'\b(?:[a-zA-Z0-9]+(?:[._-][a-zA-Z0-9]+)*)@(?:[a-zA-Z]+(?:-[a-zA-Z]+)*\.[a-zA-Z]+(?:\.[a-zA-Z]+)*)\b'
matches = re.findall(regex, text)

for email in matches:
    print(email)
