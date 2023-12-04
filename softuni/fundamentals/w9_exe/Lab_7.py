n = int(input())
synonyms_full = {}

for i in range(n):
    word = input()
    synonym = input()

    if word in synonyms_full:
        synonyms_full[word].append(synonym)
    else:
        synonyms_full[word] = [synonym]

for k, v in synonyms_full.items():
    string = ', '.join(v)
    print(f"{k} - {string}")

