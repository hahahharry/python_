# word = input()
#
# for i in range(len(word) - 1, -1, -1):
#     print(word[i] ,end = '')


word = input()
rev_word = ""

for i in range(len(word)-1, -1, -1):
    rev_word += word[i]
print(rev_word)