# str_1 = input()
# str_2 = input()
# letters = len(str_1)
# new_word_1 = ""
#
# for i in range(letters):
#
#     for j in range(letters):
#
#         curr_symbol_1 = str_1[i]
#         curr_symbol_2 = str_2[j]
#
#         new_symbol_1 = curr_symbol_2
#         new_symbol_2 = curr_symbol_1
#
#         new_word_1 += new_symbol_1
#
#
#     print(new_word_1)
#     break

first_string = input()
second_string = input()
last_printed_string = first_string
for character_index in range(len(first_string)):
    left_part = second_string[:character_index + 1]
    right_part = first_string[character_index + 1:]
    new_string = left_part + right_part
    if new_string != last_printed_string:
        print(new_string)
        last_printed_string = new_string