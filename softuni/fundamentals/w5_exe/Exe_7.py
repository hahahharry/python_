num_seq = [int(x) for x in input().split(", ")]
curr_group = 10

while num_seq:
    filtered_nums = [y for y in num_seq if y <= curr_group]
    print(f"Group of {curr_group}'s: {filtered_nums}")
    curr_group += 10
    num_seq = [z for z in num_seq if z not in filtered_nums]

