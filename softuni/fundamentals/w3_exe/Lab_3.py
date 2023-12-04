num = int(input())
positives = []
negatives = []

for _ in range(num):
    curr_num = int(input())

    if curr_num >= 0:
        positives.append(curr_num)
    else:
        negatives.append(curr_num)

print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}')
print(f'Sum of negatives: {sum(negatives)}')
