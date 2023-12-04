import re

text = "_ (Underscores) are also word characters!"
pattern = r"\w+"
result = re.findall(pattern, text)
print(result)