def perfect_num(a):
    dividers = []
    for i in range(1, a):
        if a % i == 0:
            dividers.append(i)

    sum_dividers = sum(dividers)

    if sum_dividers == a:
        return f"We have a perfect number!"
    else:
        return f"It's not so perfect."

num = int(input())
print(perfect_num(num))