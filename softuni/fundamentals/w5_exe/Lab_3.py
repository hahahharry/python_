def to_do():
    notes = []

    while True:
        cmd = input()

        if cmd == "End":
            break

        notes.append(cmd)

    sorted_notes = sorted(notes, key=lambda x: int(x.split("-")[0]))
    return [cmd.split("-")[1] for cmd in sorted_notes]

result = to_do()
print(result)
