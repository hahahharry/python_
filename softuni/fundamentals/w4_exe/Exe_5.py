num_str = input().split()
num_dig = []

for i in num_str:
    num_dig.append(int(i))

even = lambda x: x % 2 == 0 # will return True or False
result = filter(even, num_dig)
print(list(result))

