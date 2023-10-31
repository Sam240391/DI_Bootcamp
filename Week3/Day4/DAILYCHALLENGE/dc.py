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


