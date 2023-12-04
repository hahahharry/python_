def sorter(a):
    str_list = a.split()
    int_list = list(map(int, str_list))
    sorted_list = sorted(int_list)
    return sorted_list

str_input = input()
print(sorter(str_input))
