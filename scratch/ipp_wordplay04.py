import scrabble

"""
#word = "apple" # test for False
word = "radar" # test for True

is_palindrome = True

for index in range(len(word)):
    if word[index] != word[-(index + 1)]:
        is_palindrome = False
print(is_palindrome)
"""
longest = ""
"""
for word in scrabble.wordlist:
    is_palindrome = True
    for index in range(len(word)):
        if word[index] != word[-(index + 1)]:
            is_palindrome = False
    if is_palindrome and len(word) > len(longest):
        longest = word

print(longest)
"""

for word in scrabble.wordlist:
    if word == word[::-1] and len(word) > len(longest):
        longest = word

print(longest)
