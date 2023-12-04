banned = input().split(", ")
text = input()

for word in banned:
    if word in text:
        text = text.replace(word, "*"*len(word))
print(text)
