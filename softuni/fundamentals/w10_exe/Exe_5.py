text = input()

for index in range(len(text)):
    if text[index] == ":":
        emoji = ":" + text[index+1]
        print(emoji)

