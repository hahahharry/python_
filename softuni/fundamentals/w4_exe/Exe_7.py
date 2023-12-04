def another_math_func(a):
    str_list = a.split()
    int_list = list(map(int, str_list))
    max_num = max(int_list)
    min_num = min(int_list)
    sum_num = sum(int_list)
    result = f"The minimum number is {min_num}" f"\nThe maximum number is {max_num}" f"\nThe sum number is: {sum_num}"
    return result

str_input = input()
print(another_math_func(str_input))