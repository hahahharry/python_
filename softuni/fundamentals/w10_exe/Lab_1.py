while True:
    cmd = input()

    if cmd == "end":
        break
    else:
        print(f"{cmd} = {cmd[::-1]}")