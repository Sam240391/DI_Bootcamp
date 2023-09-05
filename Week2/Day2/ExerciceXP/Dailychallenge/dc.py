
# Instructions
# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples

# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

# -------------------

# number = int(input("Enter a number: "))
# length = int(input("Enter a length: "))

# multiples_list = []

# for i in range(1, length + 1):
#     multiple = number * i
#     multiples_list.append(multiple)

# print("List of multiples:")
# print(multiples_list)


# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Examples

# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"

# user's word : "ttiiitllleeee" ➞ "title"

# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
# Notes
# Final strings won’t include words with double letters (e.g. “passing”, “lottery”).


# user_input = input("Enter a string: ")

# result = ""

# for i in range(len(user_input)):
#     if i == len(user_input) - 1 or user_input[i] != user_input[i + 1]:
#         result += user_input[i]

# print("String with consecutive duplicates removed:", result)

# --------------------

user_input = input("Enter a string: ")

result = user_input[0]

# result = t

for number in range(1, len(user_input)):
    if  user_input[number] != result[-1]:
        result += user_input[number]


print(result)




