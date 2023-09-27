# Count Occurence
# Write a program which takes a string and a character as an input, and finds out the number of occurrences the character has in the string.

# String: Programming is cool!
# Character: o
# 3


# String: This is a great example
# Character: y
# 0

sentence = input('enter a sentence')
letter = input('enter a letter')

occurence = 0

for character in sentence:
    if character == letter:
        occurence += 1

print(f'the lettre {letter} is {occurence} times in {sentence}')