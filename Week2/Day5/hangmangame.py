import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']

word = random.choice(wordslist)

guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '*'
    return displayed_word

while True:
    current_display = display_word(word, guessed_letters)
    print(f"Word: {current_display}")

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a valid single letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)
    
    if current_display == word:
        print(f"Congratulations! You've guessed the word: {word}")
        break

    if guess in word:
        print("Good guess!")
    else:
        print("Incorrect guess!")
        incorrect_guesses += 1


    if incorrect_guesses == 1:
        print('O')

    if incorrect_guesses == 2:
        print('O')
        print('|')

    if incorrect_guesses == 3:
        print(' O')
        print('-|')

    if incorrect_guesses == 4:
        print(' O')
        print('-|-')

    if incorrect_guesses == 5:
        print(' O')
        print('-|-')
        print('/ ')

    if incorrect_guesses == max_attempts:
        print("Game over! You've run out of attempts.")
        print(f"The word was: {word}")
        break

    