text = input().split()
final_text = [cmd * len(cmd) for cmd in text]

print("".join(final_text))
