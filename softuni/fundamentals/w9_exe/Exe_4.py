phonebook = {}

while True:
    cmd = input()
    if "-" not in cmd:
        break
    name, number = cmd.split("-")
    phonebook[name] = number

num = int(cmd)
for i in range(num):
    cmd_names = input()
    if cmd_names in phonebook.keys():
        print(f"{cmd_names} -> {phonebook[cmd_names]}")
    else:
        print(f"Contact {cmd_names} does not exist.")
