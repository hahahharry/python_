electrons = int(input())
shell = []

for i in range(1, electrons + 1):
    layer = 2 * i**2

    if electrons >= layer:
        shell.append(layer)
        electrons -= layer
    else:
        shell.append(electrons)
        break

print(shell)