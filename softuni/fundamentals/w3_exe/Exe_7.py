gifts = input().split()

while True:
    command = input().split()
    action = command[0]

    if action == "No":
        break

    if action == "OutOfStock":
        gift_to_remove = command[1]
        for i in range(len(gifts)):
            if gifts[i] == gift_to_remove:
                gifts[i] = "None"
    elif action == "Required":
        gift_to_replace = command[1]
        index_to_replace = int(command[2])
        if 0 <= index_to_replace < len(gifts):
            gifts[index_to_replace] = gift_to_replace
    elif action == "JustInCase":
        gifts[-1] = command[1]

# Step 3: Print the final list of gifts without "None" values
filtered_gifts = [gift for gift in gifts if gift != "None"]
print(" ".join(filtered_gifts))