cmd = [char for char in input() if char != " "]
symbols = {}

for i in cmd:
    if i not in symbols.keys():
        symbols[i] = 0
    symbols[i] += 1

for k, v in symbols.items():
    print(f"{k} -> {v}")



