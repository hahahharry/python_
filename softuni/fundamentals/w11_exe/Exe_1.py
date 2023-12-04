import re

def extract_numbers(input_strings):
    numbers = re.findall(r'\d+', input_strings)
    return ' '.join(numbers)

input_lines = []
while True:
    line = input()
    if not line:
        break
    input_lines.append(line)

input_strings = '\n'.join(input_lines)
result = extract_numbers(input_strings)
print(result)
