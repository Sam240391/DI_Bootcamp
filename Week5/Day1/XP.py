
# 🌟 Exercise 1: Identifying Time Complexity
# Instructions
# Identifying the Time Complexity for each of the below programs
    
# Snippet 1

# for i in range(10):
#     print(i)

# Snippet 2

# for i in range(n):
#     for j in range(n):
#         print(i, j)

# Snippet 3

# i = 1
# while i < n:
#     i *= 2
#     print(i)


# Snippet 1 is O(n).
# Snippet 2 is O(n^2).
# Snippet 3 is O(log n).



# 🌟 Exercise 2: Understanding Insertion Sort
# Instructions
# Insertion Sort is an in-place, stable sorting algorithm that works in a manner similar to sorting a hand of playing cards. It sorts the array by moving each element to its correct position in the sorted part of the array.


# numbers = [5, 2, 9, 1, 5, 6]

# print(min(numbers))

# def insertion_sort(numbers: list) -> None:
#    for i in range(1, len(numbers)):
#       value = numbers[i]
#       j = i - 1
#       while value < numbers[j] and j >= 0:
#          numbers[j + 1] = numbers[j]
#          j -= 1
#       numbers[j + 1] = value


# def insertion_sort(numbers: list) -> None:
#     numbers_sorted = []
#     for i in range(len(numbers)):
#         numbers_sorted.append(min(numbers))
#         numbers.remove(min(numbers))

#     print(numbers_sorted)


# insertion_sort(numbers)
# print(numbers)

# 🌟 Exercise 3: Understanding Binary Search
# Instructions
# Binary Search is an efficient algorithm for finding a target value within a sorted array. Unlike linear search, which checks each element in order, binary search divides the array in half and eliminates half of the remaining elements in each iteration.

# numbers = [1, 3, 5, 7, 9, 11]
# def binary_search(numbers: list, value: int) -> int:
#     low = 0
#     high = len(numbers) - 1

#     while low <= high:
#         mid = (low + high) // 2

#         if numbers[mid] == value:
#             print(f'Target {value} found at index {mid}.') 
#             break
#         elif numbers[mid] < value:
#             low = mid + 1
#         else:
#             high = mid -1


# binary_search(numbers, 7)