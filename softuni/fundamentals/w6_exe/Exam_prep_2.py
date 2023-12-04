initial_list = input().split("!")
final_list = initial_list

while True:
    cmd = input()

    if cmd == "Go Shopping!":
        break

    cmd = cmd.split()

    if cmd[0] == "Urgent":
        first_item = cmd[1]
        if first_item not in final_list:
            final_list.insert(0, first_item)
    elif cmd[0] == "Unnecessary":
        unwanted_item = cmd[1]
        if unwanted_item in final_list:
            final_list.remove(unwanted_item)
    elif cmd[0] == "Correct":
        old_item = cmd[1]
        new_item = cmd[2]
        if old_item in final_list:
            index = final_list.index(old_item)
            final_list[index] = new_item
    elif cmd[0] == "Rearrange":
        rearr_item = cmd[1]
        if rearr_item in final_list:
            final_list.remove(rearr_item)
            final_list.append(rearr_item)

print(", ".join(final_list))