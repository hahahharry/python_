import re

text = """
I am born on 30-Dec-1994.
My father is born on the 9-Jul-1955.
01-July-2000 is not a valid date.
"""
valid_date_format = r"\b\d{1,2}-[A-Z][a-z]{2}-\d{4}\b"
result = re.findall(valid_date_format, text)

for match in result:
    print("".join(match))