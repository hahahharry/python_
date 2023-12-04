import re

raw_text = """
valid123@email.bg
invalid*name@emai1.bg
hari@abv.bg
_hari@a1.c
12hari34@gmail.eu
12hari34@@gmail.com
"""
text = raw_text.split()

validation = r"^\w+@\w+.\w+"

for email in text:
    if re.match(validation, email):
        print(f"{email} is valid.")
    else:
        print(f"{email} is NOT valid.")
