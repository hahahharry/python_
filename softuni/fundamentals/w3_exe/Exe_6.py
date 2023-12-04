num_list = input()
ref_num_list = num_list.split(" ")
int_num_list = list(map(int, ref_num_list))

num = int(input())
n = 0


smallest_nums = []

while n < num:
    smallest = min(int_num_list)

    smallest_nums.append(smallest)
    int_num_list.remove(smallest)
    n += 1

print(', '.join(map(str, int_num_list)))


