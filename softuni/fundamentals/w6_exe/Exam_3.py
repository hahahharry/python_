phones = input().split(", ")

while True:
    cmd = input()
    if cmd == "End":
        break

    command_parts = cmd.split(" - ")
    action = command_parts[0]

    if action == "Add":
        phone = command_parts[1]
        if phone not in phones:
            phones.append(phone)
    elif action == "Remove":
        phone = command_parts[1]
        if phone in phones:
            phones.remove(phone)
    elif action == "Bonus phone":
        phone_parts = command_parts[1].split(":")
        old_phone = phone_parts[0]
        new_phone = phone_parts[1]
        if old_phone in phones:
            index = phones.index(old_phone)
            phones.insert(index + 1, new_phone)
    elif action == "Last":
        phone = command_parts[1]
        if phone in phones:
            phones.remove(phone)
            phones.append(phone)

print(", ".join(phones))
