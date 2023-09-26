# Daily Challenge GOLD: Caesar Cypher
# Last Updated: September 22nd, 2023

# What You Will Learn :
# Python Basics
# Conditionals
# Loops


# Instructions
# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

# For example, with a left shift of 3 –> D would be replaced by A,
# –> E would become B, and so on.

# The method is named after Julius Caesar, who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages with ceasar cypher.
# The user enters the program, and then the program asks him if he wants to encrypt or decrypt, and then execute encryption/decryption on a given message and a given shift.

# Check out this tutorial

# Hint:
# text = 'hello how are you ?'
# cypher_text = ''
# for letter in text:
#     cypher_text += chr(ord(letter) + 3)

# print(f'{cypher_text}')



print('hello')


while True:
    user_input = input("Choose 'E' for encryption or 'D' for decryption (Q to quit):")


    if user_input.upper() == 'Q':
        break
    elif user_input.upper() == 'E':
        user_message = input(f'Write you message to encrypt')
        shift = input(f'Enter the shitf you want')
        cypher_text = ''

        for letter in user_message:
            if letter.isalpha():
                if letter.isupper():
                    cypher_text += chr((ord(letter) - ord('A') + int(shift)) % 26 + ord('A'))
                elif letter.islower():
                    cypher_text += chr((ord(letter) - ord('a') + int(shift))  % 26 + ord('a'))
            else:
                cypher_text += letter
        
        print(f'Encrypted message: {cypher_text}')

    elif user_input.upper() == 'D':
        user_message = input(f'Write you message to Decrypt')
        shift = input(f'Enter the shitf you want')
        decrypt_text = ''

        for letter in user_message:
            if letter.isalpha():
                if letter.isupper():
                    decrypt_text  += chr((ord(letter) - ord('A') - int(shift)) % 26 + ord('A'))
                elif letter.islower():
                    decrypt_text  += chr((ord(letter)  - ord('a') - int(shift)) % 26 + ord('a'))
            else:
                decrypt_text  += letter

        print(f'Encrypted message: {decrypt_text}')
    
    else:
        print("Invalid choice. Please choose 'E', 'D', or 'Q'.") 

        










