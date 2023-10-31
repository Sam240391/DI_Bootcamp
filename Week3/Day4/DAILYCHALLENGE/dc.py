# import os # operating system

# dir_path = os.path.dirname(os.path.realpath(__file__))



class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.split()
        word_count = words.count(word)
        return f'The word "{word}" appears {word_count} times in the text.'
    

    def most_common_word(self):
        words = self.text.split()
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        most_common = max(word_count, key=word_count.get)
        return f'The most common word is "{most_common}".'

    def unique_words(self):
        words = self.text.split()
        unique_words = list(set(words))
        return unique_words
    
    @classmethod
    def from_file(cls, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            return cls(text)
        except FileNotFoundError:
            return None





text_sample = "A good book would sometimes cost as much as a good house."
text_instance = Text(text_sample)

print(text_instance.word_frequency("good"))
print(text_instance.most_common_word())
print(text_instance.unique_words())


import string
from nltk.corpus import stopwords
import re

class TextModification(Text):
    def __init__(self, text):
        super().__init__(text)

    def remove_punct(self):
        translator = str.maketrans('', '', string.punctuation)
        text_no_punct = self.text.translate(translator)
        return text_no_punct

    def remove_stopwords(self):
        import nltk
        nltk.download('stopwords')
        english_stopwords = set(stopwords.words("english"))     

        words_list = self.text.split()

        filtered_words = [word for word in words_list if word.lower() not in english_stopwords]

        text_no_stopwords = " ".join(filtered_words)
        return text_no_stopwords

    def remove_spec_char(self):
        text_no_spec_chars = re.sub(r'[^A-Za-z0-9\s]', '', self.text)
        return text_no_spec_chars

