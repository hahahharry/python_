n = int(input())

for i in range(1, n + 1):
    curr_num_str = str(i)
    check_sum = 0
    for j in curr_num_str:
        check_sum += int(j)
    special_num = False

    if check_sum == 5 or check_sum == 7 or check_sum == 11:
        special_num = True

    print(f"{i} -> {special_num}")


