import re

text = input()
keyword = input()

regex = re.compile(r'\b' + re.escape(keyword) + r'\b', re.IGNORECASE)
result = re.findall(regex, text)

print(len(result))