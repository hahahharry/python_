def rounding(numbers):
    rounded_list = []
    for i in numbers:
        curr_num = round(i)
        rounded_list.append(curr_num)
    return rounded_list

nums = input().split(" ")
nums_int_list = list(map(float, nums))

print(rounding(nums_int_list))
