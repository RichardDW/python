import scrabble
import string

# Find if there are letters which are 
# never used double in the scrabble dictionary

for letter in string.ascii_lowercase:
    exists = False
    for word in scrabble.wordlist:
        if letter * 2 in word:
            exists = True
            print(word,"\n")
            break
    if not exists:
        print("There are no English words with a double " + letter)

    
