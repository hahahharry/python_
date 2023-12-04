def ascii_converter(a, b):
    ascii_list = []
    initial = ord(a) + 1
    final = ord(b)
    for i in range(initial, final):
        ascii_sym = chr(i)
        ascii_list.append(ascii_sym)
        final_str = " ".join(ascii_list)

    return final_str

a, b = input(), input()
print(ascii_converter(a, b))