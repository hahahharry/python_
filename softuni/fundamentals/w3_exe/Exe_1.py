symbols = input()

filtered_symbols = symbols.split(" ")
new_list = []

for i in filtered_symbols:
    curr_num = int(i) * (-1)
    new_list.append(curr_num)

print(new_list)