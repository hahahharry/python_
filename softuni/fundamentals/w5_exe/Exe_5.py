def room_check(rooms):
    free_chairs = 0
    for rooms in range(1, rooms + 1):
        chairs_curr_room, visitors = input().split()
        diff = len(chairs_curr_room) - int(visitors)

        if diff < 0:
            print(f"{abs(diff)} more chairs needed in room {rooms}")
        free_chairs += diff

    return free_chairs

rooms_input = int(input())
total_free_chairs = room_check(rooms_input)

if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")

