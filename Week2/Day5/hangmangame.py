import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 

### YOUR CODE STARTS FROM HERE ###

def hiddingword():

    for letter in word:
        print('*', end='')
    



def playergame():
    turn = 0
    hiddingword()

    winword = ''

    while True:
        try:
            letter_player = input(f"Player, enter a letter")
            if letter_player in word:
                word.replace('*', letter_player)
                print(f'{letter_player} is in the word')
                winword.join({letter_player})
                print(winword)
            else:
                print(f'{letter_player} is not in word')
                turn += 1
            
            if turn == 1:
                print('be Carefull')
                print('O')
            elif turn == 2:
                print('O')
                print('|')
            elif turn == 3:
                print(' O ')
                print('-| ')
            elif turn == 4:
                print(' O ')
                print('-|-')
            elif turn == 5:
                print(' O ')
                print('-|-')
                print('/ ')
            elif turn == 6:
                print(' O ')
                print('-|-')
                print('/ I')
                print('you loose')
                break


        except ValueError:
            print("Invalid input..")


playergame()