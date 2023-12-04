parking_database = {}

num = int(input())

for i in range(num):
    cmd = input().split()

    if "unregister" in cmd:
        username = cmd[1]

        if username not in parking_database:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking_database[username]

    else:
        username = cmd[1]
        lic_plate = cmd[2]

        if username not in parking_database:
            parking_database[username] = lic_plate
            print(f"{username} registered {lic_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_database[username]}")

for k, v in parking_database.items():
    print(f"{k} => {v}")
