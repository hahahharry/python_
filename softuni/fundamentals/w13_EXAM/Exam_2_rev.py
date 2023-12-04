import re

def encrypt_password(password):
    pattern = r"(.{1,})>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<(\1)"
    match = re.match(pattern, password)
    if match:
        encrypted = ''.join(match.group(i) for i in range(2, 6))
        return f"Password: {encrypted}"
    else:
        return "Try another password!"

num_inputs = int(input())

for _ in range(num_inputs):
    user_input = input()
    result = encrypt_password(user_input)
    print(result)
