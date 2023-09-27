# Instructions
# Given a “Matrix” string:

#     7ii
#     Tsx
#     h%?
#     i #
#     sM 
#     $a 
#     #t%
#     ^r!


# The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
# A grid means that you could potentially break it into rows and columns, like here:

# 7	i	3
# T	s	i
# h	%	x
# i		#
# s	M	
# $	a	
# #	t	%
# ^	r	!


# Matrix: A matrix is a two-dimensional array. It is a grid of numbers arranged in rows and columns.
# To reproduce the grid, the matrix should be a 2D list, not a string



# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, selecting only the alpha characters and connecting them. Then he replaces every group of symbols between two alpha characters by a space.

# Using his technique, try to decode this matrix.

# Hints:
# Use
# ● lists for storing data
# ● Loops for going through the data
# ● if/else statements to check the data
# ● String for the output of the secret message

# Hint (if needed) : Look at the remote learning “Matrix” videos



# matrix_string = """\
# 7ii
# Tsx
# h%?
# i #
# sM 
# $a 
# #t%
# ^r!"""




# matrix = [list(row) for row in matrix_string.splitlines()]
# matrix_rows = matrix_string.splitlines()

# print(matrix)

# num_columns = len(matrix[0])
# print(num_columns)

# decoded_message = []

# for col in range(num_columns):
#     column_data = []  
#     for row in range(len(matrix)):
#         char = matrix[row][col]
#         if char.isalnum():  
#             column_data.append(char)
  
#     decoded_message.extend(column_data)

# decoded_message = ''.join(decoded_message)

# # Print the decoded message
# print(decoded_message)


secret = """7i3
Tsi
h%x
i #
sM 
$a 
#t%
^r!"""

def create_colums() :
    secret_list = list(secret.split("\n"))
    lst = []
    for num in range(3) :
        lst.append([char[num] for char in secret_list])

    return lst

def decode() :
    secret = create_colums()
    # print("secret list", secret)
    final = ""
    for arr in secret :
        for char in arr :
            if str(char).isalpha() :
                    final += char
            else :
                final += " "
    print(final)

decode()