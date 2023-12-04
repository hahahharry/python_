char_index_1 = int(input())
char_index_2 = int(input())

for i in range(char_index_1, char_index_2 + 1):
    asc_sym = chr(i)
    print(f"{asc_sym}", end = " ")
