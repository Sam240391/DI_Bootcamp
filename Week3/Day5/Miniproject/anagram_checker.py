import os # operating system

dir_path = os.path.dirname(os.path.realpath(__file__))
import nltk
# nltk.download('words')
from nltk.corpus import words as nltk_words


class AnagramChecker:
    def __init__(self, words):
        with open(dir_path + '\\' + words, "r") as word_list_file :
            self.words = tuple(word_list_file.read().split())
        

    def is_valid_word(self, word):
        word = word.upper()
        if word in self.words:
            return True
        else:
            return False

    def get_anagrams(self, word):
        from itertools import permutations
        word = word.lower()
        anagrams_list = []
        for anagram in permutations(word):
                anagrams_list.append(''.join(anagram))
        anagrams_list.remove(str(word))
        anagrams = []
        for word in anagrams_list:
            if self.is_valid_word(word):
                anagrams.append(word)
        return anagrams

    def is_anagram(self, word1, word2):
            if sorted(word1) == sorted(word2):
                 return True
            else:
                return False


my_words = AnagramChecker('word_list.txt')
print(my_words.is_valid_word('without'))
# print(my_words.get_anagrams('car'))
# print(my_words.is_anagram('car', 'cra'))


