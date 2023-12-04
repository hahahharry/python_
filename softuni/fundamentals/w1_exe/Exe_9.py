
while True:
    name = input()

    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    elif name == "Voldemort":
        print("You must not speak of that name!")
        break
    else:

        if len(name) < 5:
            house = "Gryffindor"
        elif len(name) == 5:
            house = "Slytherin"
        elif len(name) == 6:
            house = "Ravenclaw"
        else:
            house = "Hufflepuff"

        print(f"{name} goes to {house}.")