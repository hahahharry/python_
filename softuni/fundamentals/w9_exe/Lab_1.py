dict_elements = input().split()
my_dict = {}

for i in range(0, len(dict_elements), 2):
    food = dict_elements[i]
    quantity = int(dict_elements[i+1])
    my_dict[food] = quantity

print(my_dict)