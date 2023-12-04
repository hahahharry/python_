# curr_year = int(input())
# check = False
#
# while not check:
#     curr_year += 1
#
#     check = True
#     for i in str(curr_year):
#         if str(curr_year).count(i) > 1:
#             check = False
#             break
#
# print(curr_year)

curr_year = int(input())

while True:
    curr_year += 1
    curr_year_str = str(curr_year)
    if len(curr_year_str) == len(set(curr_year_str)):
        break

print(curr_year)
