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



# Iteration Over the String:
# The function iterates over each character in the string s exactly once. This gives a time complexity of (O(n)).
# Stack Operations:
# Pushing an element onto the stack and popping an element from the stack both take (O(1)) time. 
# Since each character is pushed and popped at most once, the total time for stack operations is (O(n)).
# Dictionary Lookups:
# Checking if a character is in the dictionary and accessing the dictionary values both take (O(1)) time.
# Combining these factors, the overall time complexity of the function is (O(n)).