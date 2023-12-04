import re

text = input()
format = '\\b[A-Z][a-z]+ +[A-Z][a-z]+\\b'
result = re.findall(format, text)

for i in result:
    print(i, end=" ")
