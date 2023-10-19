from googletrans import Translator


translator = Translator()

# dt1 = translator.detect(text1)
# print(dt1)

# dt2 = translator.detect(text2)
# print(dt2)
# translated = translator.translate('Бороди́нское сраже́ние')
# print(translated.text)

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

bonjour_en = translator.translate('bonjour', src='fr', dest='es')
print(bonjour_en.text)

traduction_dict = {}

for word in french_words:
    word_en = translator.translate(word, src='fr', dest='en')
    traduction_dict[word] = word_en.text

print(traduction_dict)


