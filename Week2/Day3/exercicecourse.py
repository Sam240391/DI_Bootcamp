
# exercise

# ask the user for the fruit he wants
# depending on the fruit we show him the price
# don't use conditionals



# prices = {
#     "apple" : 2,
#     "banana" : 5,
#     "orange" : 1
# }


# fruit = input("What fruit do you want? ").lower()

# print(f"The price of {fruit} is {prices[fruit]}")




# words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']

# uppercased_words = [word for word in words if word.isupper()]

# print(uppercased_words)



# Exercise 3
# Print the total duration of the playlist

# playlist = {
#     'title': "Hello World",
#     'author': "Planet",
#     'songs': [
#         {
#             'song_title': "Song One",
#             'artist': ['Artist 1', 'Artist 2'],
#             'duration': 4.31,
#         },
#         {
#             'song_title': "Song Two",
#             'artist': ['Artist 1'],
#             'duration': 2.53,
#         },
#         {
#             'song_title': "Song Three",
#             'artist': ['Artist 1', 'Artist 2', 'Artist 3'],
#             'duration': 3.43,
#         }
#     ]
# }


# for i in range(len(playlist['songs'])):
#     print (playlist['songs'][i][("duration")])



# total_duration = 0 



# for song in playlist['songs']:
#     total_duration += song["duration"]


# print(total_duration)





rick_dict = {
    'first_name':'Rick',
    'last_name':'Sanchez'
}

set_rick = rick_dict.items()
print(set_rick)