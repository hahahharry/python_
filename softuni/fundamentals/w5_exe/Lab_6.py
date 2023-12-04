
nums = list(map(int, input().split(', ')))
indeces = map(lambda x: x if nums[x] % 2 == 0 else 'no', range(len(nums)))
even_indeces = list(filter(lambda y: y != 'no', indeces))
print(even_indeces)