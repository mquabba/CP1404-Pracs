import random

VOWELS = "aeiou"
CONSONANTS = "npqyzbcdfgrstvwxhjklm"

word_format = "ccvcvvc"
word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

print(word)