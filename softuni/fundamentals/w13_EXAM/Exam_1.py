msg = input()

while True:
    cmd = input().split()
    if cmd[0] == "Finish":
        break

    if cmd[0] == "Replace":
        current_char = cmd[1]
        new_char = cmd[2]
        msg = msg.replace(current_char, new_char)
        print(msg)

    elif cmd[0] == "Cut":
        start_index = int(cmd[1])
        end_index = int(cmd[2])

        if 0 <= start_index < len(msg) and 0 <= end_index < len(msg):
            if start_index <= end_index:
                msg = msg[:start_index] + msg[end_index + 1:]
                print(msg)
            else:
                print("Invalid indices!")
        else:
            print("Invalid indices!")

    elif cmd[0] == "Make":
        case = cmd[1]
        if case == "Upper":
            msg = msg.upper()
        elif case == "Lower":
            msg = msg.lower()
        print(msg)

    elif cmd[0] == "Check":
        string_to_check = cmd[1]
        if string_to_check in msg:
            print(f"Message contains {string_to_check}")
        else:
            print(f"Message doesn't contain {string_to_check}")

    elif cmd[0] == "Sum":
        start_index = int(cmd[1])
        end_index = int(cmd[2])

        if 0 <= start_index < len(msg) and 0 <= end_index < len(msg):
            if start_index <= end_index:
                substring = msg[start_index:end_index + 1]
                ascii_sum = sum(ord(char) for char in substring)
                print(ascii_sum)
            else:
                print("Invalid indices!")
        else:
            print("Invalid indices!")
