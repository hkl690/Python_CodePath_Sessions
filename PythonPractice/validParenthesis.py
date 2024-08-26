# Your function isValid is called as such:
# s = "()"
# isValid(s)

def isValid(s: str) -> bool:
    stack = []
    matching_dict = {')':'(', '}':'{', ']':'['}

    # Remove whitespace from the string
    s = ''.join(s.split())

    for char in s:
        if char in matching_dict.values():
            # If it is an opening parenthesis, push onto the stack
            stack.append(char)
        elif char in matching_dict.keys():
            # If it is a closing parenthesis, check for matching value
            if stack == [] or matching_dict[char] != stack.pop():
                return False
        else: # If it's an invalid character, return False
            return False
    # Ensure the stack is empty at the end
    return stack == [] 


# Example 1
s = "()"
print(isValid(s)) # True

# Example 2
s = "()[ ]{}" # has whitespace
print(isValid(s)) # True after taking out whitespace, else False

# Example 3
s = "(]"
print(isValid(s)) # False

# Example 4
s = "()[]{}" # no whitespace
print(isValid(s)) # True