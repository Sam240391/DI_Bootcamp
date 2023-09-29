# Exercise 1
# Instructions
# Write a script that inserts an item at a defined index in a list.

# fruits = ['orange', 'banana', 'apple', 'pear', 'melon']

# def insert_item_at_index(my_list, item, index):
#     my_list.insert(index, item)

# insert_item_at_index(fruits, 'watermelon', 2)

# print(fruits)

# Exercise 2
# Instructions
# Write a script that counts the number of spaces in a string.

# def count_space_in_str(my_string):
#     count_space = my_string.count(' ')
#     return count_space

# print(count_space_in_str('hello comment cava toi '))


# Exercise 3
# Instructions
# Write a script that calculates the number of upper case letters and lower case letters in a string.

# def count_upper_in_string(my_string):
#     number_of_upper_character = 0
#     number_of_lower_character = 0
#     for character in my_string:
#         if character.isupper():
#             number_of_upper_character +=1
#         elif character.islower():
#             number_of_lower_character +=1

#     print(f'In the Sentence you have {number_of_upper_character} upper characters and {number_of_lower_character} lower characters')

# count_upper_in_string('HEllo Comment CaVa')

# Exercise 4
# Instructions
# Write a function to find the sum of an array without using the built in function:

#     >>>my_sum([1,5,4,2])
#     >>>12

# def my_sum(array):
#     my_sum = 0
#     for i in array:
#         my_sum += i
    
#     print(my_sum)

# my_sum([1,5,4,2])



# Exercise 5
# Instructions
# Write a function to find the max number in a list

#     >>>find_max([0,1,3,50])
#     >>>50


# def find_max(my_list):
#     my_bigger_number = 0
    
#     for number in my_list:
#         if number > my_bigger_number:
#             my_bigger_number = number

#     print(my_bigger_number)

# find_max([0,1,3,50])


# Exercise 6
# Instructions
# Write a function that returns factorial of a number

#     >>>factorial(4)
#     >>>24

# def factorial(n):
#     result = 1
#     for x in range(1, n + 1):
#           result *= x
    
#     print(result)


# factorial(4)


# Exercise 7
# Instructions
# Write a function that counts an element in a list (without using the count method):

#     >>>list_count(['a','a','t','o'],'a')
#     >>>2

# def list_count(my_list, element):
#     number_element = 0
#     for character in my_list:
#         if character == element:
#             number_element += 1

#     print(number_element)

# list_count(['a','a','t','o'],'a')


# Exercise 8
# Instructions
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

#     >>>norm([1,2,2])
#     >>>3

# import math

# def norm(my_list):
#     square_root = 0
#     list_squared = []

#     for number in my_list:
#         list_squared.append(number*number)
    
#     sum_squared = sum(list_squared)
#     result = math.sqrt(sum_squared)
    
#     print(result)



# norm([1,2,2])


# Exercise 9
# Instructions
# Write a function to find if an array is monotonic (sorted either ascending of descending)

#     >>>is_mono([7,6,5,5,2,0])
#     >>>True

#     >>>is_mono([2,3,3,3])
#     >>>True

#     >>>is_mono([1,2,0,4])
#     >>>False


# def is_mono(arr):
#     increasing = decreasing = True

#     for i in range(1, len(arr)):
#         if arr[i] < arr[i - 1]:
#             increasing = False
#         if arr[i] > arr[i - 1]:
#             decreasing = False

#     return increasing or decreasing
    
# # Test the function
# arr1 = [7, 6, 5, 5, 2, 0]
# arr2 = [2, 3, 3, 3]
# arr3 = [1, 2, 0, 4]

# print(is_mono(arr1))  # Output: True
# print(is_mono(arr2))  # Output: True
# print(is_mono(arr3))  # Output: False

# Exercise 10
# Instructions
# Write a function that prints the longest word in a list.

# def longest_word_in_sentence(sentence):
#     words = sentence.split()

#     longest_word = ''

#     for word in words:
#         if len(word) > len(longest_word):
#             longest_word = word
    
#     return longest_word

# print(longest_word_in_sentence('Hello comment cava toi cette semaine'))

# Exercise 11
# Instructions
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.

# def separate_integers_and_strings(input_list):
#     integers = []
#     strings = []

#     for item in input_list:
#         if isinstance(item, int):
#             integers.append(item)
#         elif isinstance(item, str):
#             strings.append(item)

#     return integers, strings

# # Test the function
# mixed_list = [1, 'apple', 2, 'banana', 3, 'cherry', '4']
# integers, strings = separate_integers_and_strings(mixed_list)

# print("Integers:", integers)
# print("Strings:", strings)


# Exercise 12
# Instructions
# Write a function to check if a string is a palindrome:

#     >>>is_palindrome('radar')
#     >>>True

#     >>>is_palindrome('John)
#     >>>False



# def is_palindrome(word):

#     word_list = []

#     for letter in word:
#         word_list.append(letter)

#     for letter in word_list:
#         if len(word_list) > 1 and word_list[0] == word_list[-1]:
#             word_list.remove(word_list[0])
#             word_list.pop()

#     if len(word_list) > 1:
#         return False
#     else:
#         return True


# print(is_palindrome('bafb'))

# Exercise 13
# Instructions
# Write a function that returns the amount of words in a sentence with length > k:

#     >>>sentence = 'Do or do not there is no try'
#     >>>k=2
#     >>>sum_over_k(sentence,k)
#     >>>3




# def sum_over_k(sentence,k):
#     words = sentence.split()
#     result = 0

#     for word in words:
#         if len(str(word)) > k:
#             result +=1
    
#     return result


# sentence = 'Do or do not there is no try'
# k=2
# print(sum_over_k(sentence,k))


# Exercise 14
# Instructions
# Write a function that returns the average value in a dictionary (assume the values are numeric):

#     >>>dict_avg({'a': 1,'b':2,'c':8,'d': 1})
#     >>>3


# def dict_avg(my_dict):
#     sum_value = 0
#     for key, value in my_dict.items():
#         sum_value += value
    
#     avg_value = sum_value / len(my_dict)

#     return avg_value

# print(dict_avg({'a': 1,'b':2,'c':8,'d': 1}))


# Exercise 15
# Instructions
# Write a function that returns common divisors of 2 numbers:

#     >>>common_div(10,20)
#     >>>[2,5,10]

# divisor_x = []
# x = 10

# for i in range(1, 100):
#     if x % i == 0:
#         divisor_x.append(i)

# print(divisor_x)


# def common_div(x, y):
#     divisor_x = []
#     divisor_y = []
#     common_div = []

#     for i in range(2, x + 1):
#         if x % i == 0:
#             divisor_x.append(i)

#     for i in range(2, y + 1):
#         if y % i == 0:
#             divisor_y.append(i)

#     for elementx in divisor_x:
#         if elementx in divisor_y :
#             common_div.append(elementx)

#     print(common_div)

# common_div(10,20)


# Exercise 16
# Instructions
# Write a function that test if a number is prime:

#     >>>is_prime(11)
#     >>>True


# def is_prime(x):

#     divisor_x = []

#     for i in range(1, x+1):
#         if x % i == 0:
#             divisor_x.append(i)

#     if len(divisor_x) == 2:
#         return True
#     else: 
#         return False
    
# print(is_prime(2))

    
# Exercise 17
# Instructions
# Write a function that prints elements of a list if the index and the value are even:

#     >>>weird_print([1,2,2,3,4,5])
#     >>>[2,4]

# def weird_print(my_list):

#     result = []
#     index = 0

#     for number in my_list:
#         if number % 2 == 0  and index % 2 == 0:
#             result.append(number)

#         index += 1

#     print(result)

# weird_print([1,2,2,3,4,5])


# Exercise 18
# Instructions
# Write a function that accepts an undefined number of keyworded arguments and return the count of different types:

#     >>>type_count(a=1,b='string',c=1.0,d=True,e=False)
#     >>>int: 1, str:1 , float:1, bool:2



# def type_count(**element):
    
#     type_counts = {}

#     for key, value in element.items():
#         element_type = type(value).__name__

#         if element_type in type_counts:
#             type_counts[element_type] =+ 1
#         else:
#             type_counts[element_type] = 1


#     result = ', '.join([f"{key}: {value}" for key, value in type_counts.items()])
    
#     return result

# print(type_count(a=1,b='string',c=1.0,d=True,e=False))


# Exercise 19
# Instructions
# Write a function that mimics the builtin .split() method for strings.
# By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.


# def my_split(expr, arg=' '):
#     my_list = []
#     word1 = ''

#     for word in expr:
#         if word != arg:
#             word1 += word
#         else:
#             my_list.append(word1)
#             word1 = ''

#     print(my_list)

# my_split('hello toi, comment cava, aujourd"hui, cava', ' ')

# Exercise 20
# Instructions
# Convert a string into password format.
# Example:
# input : "mypassword"
# output: "***********"


# user_input = input(f'Enter Your password')

# output = ''

# for letter in user_input:
#     output += '*'

# print(f'{output}')