def palindrome(word):
    if word == word[::-1]:
        return word

word_input = input().split()
palindrome_example = input()

filtered_list = [word for word in word_input if palindrome(word)]
counter = filtered_list.count(palindrome_example)

print(filtered_list)
print(f"Found palindrome {counter} times")