import re

text = input()
validation = r"(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})"

result = re.findall(validation, text)

for i in result:
    day = i[0]
    month = i[2]
    year = i[3]
    separator = i[1]
    print(f"Day: {day}, Month: {month}, Year: {year}")