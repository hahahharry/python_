friends = input().split(", ")
blacklisted_names = 0
lost_names = 0

while True:
    cmd = input().split()
    action = cmd[0]

    if action == "Report":
        break

    if action == "Blacklist":
        name = cmd[1]
        if name in friends:
            index = friends.index(name)
            friends[index] = "Blacklisted"
            blacklisted_names += 1
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")
    elif action == "Error":
        index = int(cmd[1])
        if 0 <= index < len(friends) and friends[index] != "Blacklisted" and friends[index] != "Lost":
            name = friends[index]
            friends[index] = "Lost"
            lost_names += 1
            print(f"{name} was lost due to an error.")
    elif action == "Change":
        index = int(cmd[1])
        new_name = cmd[2]
        if 0 <= index < len(friends):
            current_name = friends[index]
            friends[index] = new_name
            print(f"{current_name} changed his username to {new_name}.")

print(f"Blacklisted names: {blacklisted_names}")
print(f"Lost names: {lost_names}")
print(" ".join(friends))
