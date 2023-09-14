# import random
# import os # operating system

# dir_path = os.path.dirname(os.path.realpath(__file__))

# def get_words_from_file():
      
#     with open(dir_path + r"\\word_list.txt", "r") as word_list_file :
#         words = tuple(word_list_file.read().split())
#         return words

# def get_random_sentence(length):
#     sentence_list = []
#     for _ in range(length):
#         sentence_list.append(random.choice(get_words_from_file()))
#         sentence = ' '.join(sentence_list).lower()
#     return sentence

# def main():
#     print('The program get words from a file which is in the same directory, and create a liste with all the words. and the function get random sentence will create a sentence with the words inside this list with how many words i want.')
#     lenght_sentence = input("Enter the length of the sentence (2-20):")
#     try:  
#         if lenght_sentence.isalpha():
#             raise TypeError("The lenght_sentence is not an int") 
#         if (int(lenght_sentence) <=1 or int(lenght_sentence) >= 21) and isinstance(int(lenght_sentence), int):
#             raise ValueError("the lenght sentence not beetween 2-20")    
#         else:
#             print('data accepted')
#             print(get_random_sentence(int(lenght_sentence)))
#     except ValueError as error:
#         print(error)
#         print("Probleme with the lenght your choose")
#         main()
#     except TypeError as error:
#         print(error)
#         print('Problem with the type of input')
#         main()


# the best data type is a list

# print(get_words_from_file())

# print(get_random_sentence(10))


# main()



# 🌟 Exercise 2: Working With JSON
# Instructions
# import json
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""


# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.


import json

# The JSON string
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


data = json.loads(sampleJson)
print(data)

salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)

data["company"]["employee"]["birth_date"] = "24/03/1991"

print(data)


with open(r"C:\Users\samue\Desktop\Developers Institute Course\DI_Bootcamp\Week3\Day4\XP\updated_data.json", "w") as file:
   print('test') 
   json.dump(data, file)
