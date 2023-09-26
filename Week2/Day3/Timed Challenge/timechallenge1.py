# Reverse The Sentence
# Write a program to reverse the sentence wordwise.

# Input:
# You have entered a wrong domain
# Output:
# domain wrong a entered have You


user_input = input(f' Write a sentence')

my_list = user_input.split()
reversed_list = []

for word in range(len(my_list)):
    reversed_list.append(my_list[-1])
    my_list.pop()

    
reversed_list = ' '.join(reversed_list)
print(reversed_list)


