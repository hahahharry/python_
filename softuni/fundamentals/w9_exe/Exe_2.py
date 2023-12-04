resources = {}

while True:
    cmd = input()

    if cmd == "stop":
        break
    cmd_qty = int(input())

    if cmd not in resources.keys():
        resources[cmd] = 0
    resources[cmd] += cmd_qty

for k, v in resources.items():
    print(f"{k} -> {v}")



