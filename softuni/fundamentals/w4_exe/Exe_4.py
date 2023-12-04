num = int(input())
num_str = str(num)

def sum_digits(number):
    odd_sum = []
    even_sum = []
    total_odd_sum, total_even_sum = 0, 0
    for i in number:
        curr_num = int(i)

        if curr_num % 2 == 0:
            even_sum.append(curr_num)
        else:
            odd_sum.append(curr_num)

    total_odd_sum = sum(odd_sum)
    total_even_sum = sum(even_sum)
    result = f"Odd sum = {total_odd_sum}, Even sum = {total_even_sum}"
    return result

print(sum_digits(num_str))