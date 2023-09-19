from anagram_checker import AnagramChecker


def show_menu():
     print('Welcome in our Program of anagram words')
     print('----------------')
     while True:
        user_input = input("Enter a word or 'quit' to quit: ")
        
        if user_input.lower() == 'quit':
            return None
        
        if len(user_input.split()) != 1:
            print("Error: Only a single word is allowed.")
        elif not user_input.isalpha():
            print("Error: Only alphabetic characters are allowed.")
        else:
            return user_input
        




def main():

    user_word = show_menu().upper()
    print(f'Your word is : {user_word}')
    my_words = AnagramChecker('word_list.txt')
    if my_words.is_valid_word(user_word):
        print(f' {user_word} is in my list word')
    else: 
        print(f' {user_word} is not in my list word')
        print(f'choose another word')
        main()

    anagram =my_words.get_anagrams(user_word)
    if len(anagram) > 1:
        print(f'The anagrams of {user_word} is : {" ".join(anagram[0:-1]).lower()} and {anagram[-1]}')
    else:
        print(f'There is no anagrams of {user_word} in my list')


main()