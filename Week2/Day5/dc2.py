# Instructions
# Here is a python code that generate a list of 20000 random numbers, called list_of_numbers.
# Extend this code to guess how many couples of numbers in list_of_numbers sum to target_number.

import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number   = 3728


def how_many_couple(liste_of_numbers, target_number):
    my_list = []
    i = 0

    for j in range(20000):
        if list_of_numbers[i] + list_of_numbers[j] == target_number:
            my_list.append((list_of_numbers[i], list_of_numbers[j]))
            i += 1

    result = len(my_list)
    print(my_list)

    return result


print(how_many_couple([random.randint(0, 10000) for _ in range(20000)], 3728))