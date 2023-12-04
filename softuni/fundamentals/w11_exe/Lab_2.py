import re

numbers = input()
validation = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"

result = re.findall(validation, numbers)

print(", ".join(result))