# Exercise 3 : Outputs
# Instructions
# Predict the output of the following code snippets:
#     >>> 3 <= 3 < 9
#     >>> 3 == 3 == 3
#     >>> bool(0)
#     >>> bool(5 == "5")
#     >>> bool(4 == 4) == bool("4" == "4")
#     >>> bool(bool(None))
#     x = (1 == True)
#     y = (1 == False)
#     a = True + 4
#     b = False + 10

#     print("x is", x)
#     print("y is", y)
#     print("a:", a)
#     print("b:", b)

# True
# True
# False
# False
# True
# False

# x is True
# y is False
# a: 5
# b: 11


# Exercise 4 : How Many Characters In A Sentence ?
# Instructions
# Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable).
# my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
#            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
#            Ut enim ad minim veniam, quis nostrud exercitation ullamco 
#            laboris nisi ut aliquip ex ea commodo consequat. 
#            Duis aute irure dolor in reprehenderit in voluptate velit 
#            esse cillum dolore eu fugiat nulla pariatur. 
#            Excepteur sint occaecat cupidatat non proident, 
#            sunt in culpa qui officia deserunt mollit anim id est laborum.
# ------------------------


# my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# print(len(my_text))


# Exercise 5: Longest Word Without A Specific Character
# Instructions
# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.
# ----------------



sentence_user = input(f'Write the longest sentence you can without the character "A": \n ' )

lenght_sentence =  0



if  'a' in sentence_user and len(sentence_user) > lenght_sentence :
    lenght_sentence = len(sentence_user)
    print('Congratulation it"s a new record your sentence made {lenght_sentence} ')
else:
    print(f'your sentence contains the letter a or you sentence made only {lenght_sentence} character it"s too short ')



print(lenght_sentence)

