wagons = [0] * int(input())

while True:
    cmd = input().split()

    if cmd[0] == "End":
        print(wagons)
        break
    elif cmd[0] == "add":
        people = int(cmd[1])
        wagons[-1] += people
    elif cmd[0] == "insert":
        index = int(cmd[1])
        people = int(cmd[2])
        wagons[index] += people
    elif cmd[0] == "leave":
        index = int(cmd[1])
        people = int(cmd[2])
        wagons[index] -= people
