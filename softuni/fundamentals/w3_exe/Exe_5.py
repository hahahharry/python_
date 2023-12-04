initial_deck = input().split(" ")
count = int(input())

step = len(initial_deck)//2
counter = 0

upper_half = []
lower_half = []
new_deck = []

for i in range(int(len(initial_deck)/2)):
    sym = initial_deck[i]
    upper_half.append(sym)

for k in range(int(step), int(len(initial_deck))):
    sym_2 = initial_deck[k]
    lower_half.append(sym_2)

while counter < count:
    new_deck.clear()
    for m in range(len(upper_half)):
        card_1 = upper_half[m]
        card_2 = lower_half[m]
        new_deck.append(card_1)
        new_deck.append(card_2)

    upper_half = new_deck[:(int(step))]
    lower_half = new_deck[(int(step)):]
    counter += 1

print(new_deck)
