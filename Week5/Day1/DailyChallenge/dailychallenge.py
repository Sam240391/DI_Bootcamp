
def check_balanced_parantheses(expr):

    paranthese = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }

    stack = []

    for i in expr:
        if i in paranthese.values():
            stack.append(i)
        elif i in paranthese.keys():
            if stack[-1] == paranthese[i]:
                stack.pop()
            else:
                stack.append(i)
            
    if len(stack) == 0:
        return True
    else:
        return False


expr1 = "(1 + 2) * {[(3 / 4) - 5]}"
expr2 = "[1 + 2) * (3 - 4)]"
expr3 = "((1 + 2)"
print(check_balanced_parantheses(expr2))



# Example Inputs And Outputs
# Input: "(1 + 2) * {[(3 / 4) - 5]}"
# Output: True

# Input: "[1 + 2) * (3 - 4)]"
# Output: False

# Input: "((1 + 2)"
# Output: False
