element_sequence = input().split()
moves = 0

while True:
    cmd = input()

    if cmd == "end":
        break
    else:
        index_1 = int(cmd.split()[0])
        index_2 = int(cmd.split()[1])

        if (
                index_1 == index_2
                or index_1 > len(element_sequence)
                or index_2 > len(element_sequence)
                or index_1 < 0
                or index_2 < 0
        ):
            print("Invalid input! Adding additional elements to the board")
            new_elements = f"-{moves}a"
            element_sequence.insert(len(element_sequence)//2, new_elements)
            element_sequence.insert(len(element_sequence)//2, new_elements)
        else:
            moves += 1
            if element_sequence[index_1] == element_sequence[index_2]:
                element = element_sequence[index_2]
                print(f"Congrats! You have found matching elements - {element}!")
                element_sequence.remove(element)
                element_sequence.remove(element)
            else:
                print("Try again!")

        if len(element_sequence) == 0:
            break

if len(element_sequence) == 0:
    print(f"You have won in {moves} turns!")
else:
    print("Sorry you lose :(")
    print(' '.join(map(str,element_sequence)))
