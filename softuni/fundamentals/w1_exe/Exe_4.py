divisor = int(input())
boundary = int(input())
N = 0

for i in range(1, boundary + 1):
    if i % divisor == 0:
        if i > N:
            N = i

print(f"{N}")

        