"""
Balanced Parenthesis:
Given a string containing just the characters (, ), {, }, [, and ], 
determine if the input string is valid. 

An input string is valid if the brackets are closed in the correct order.
Balanced parentheses mean that every opening parenthesis '(' has a corresponding closing parenthesis ')' in the correct order.

"""
expression = input("Enter a string: ")

def is_balanced(expression):
    stack = []
    mapping = {  # dictionary of paired values 
                ')': '(', # closing : opening 
                '}': '{', 
                ']': '['
        }

    for char in expression:
        # opening pair is checked first since its needs to be close
        if char in mapping.values(): # gets the opening pair
            stack.append(char)

        # checks for closing pair 
        elif char in mapping.keys(): 
            if (not stack) or (stack.pop() != mapping[char]):
                # checks if 
                # 1. (not stock) = the stack is empty, if its empty then its not balanced 
                # 2. (stack.pop() != mapping[char]) =  poped element is equal to its corresponding closing pair
                return False
            
        else: # Ignore non-parentheses characters
            continue

    # if the foor loop doesnt have any unbalanced parenthesis , return true 
    return True

# Example usage:
print(is_balanced(expression))


