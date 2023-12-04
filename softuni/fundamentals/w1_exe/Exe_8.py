coffee = 0

while True:
    cmd = input()

    if cmd == "END":
        break
    elif cmd == "coding" or cmd == "cat" or cmd == "dog" or cmd == "movie":
        coffee += 1
    elif cmd == "CODING" or cmd == "CAT" or cmd == "DOG" or cmd == "MOVIE":
        coffee += 2
    else:
        continue

    if coffee > 5:
        print("You need extra sleep")
        break

if coffee <= 5:
    print(f"{coffee}")