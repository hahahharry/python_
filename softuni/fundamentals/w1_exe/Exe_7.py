new_string = ""

while True:
    string = input()
    new_string = ""

    if string == "End":
        break
    elif string == "SoftUni":
        continue
    else:

        for i in range(len(string)):
            char = string[i]
            new_string += f"{char}{char}"

    print(new_string)


