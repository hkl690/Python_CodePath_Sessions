# Unit 7 Advanced A
# 6

def complex_recursive_function(arr, multiplier):
    if not arr:
        return 1
    return arr[0] * multiplier + complex_recursive_function(arr[1:], multiplier)

print(complex_recursive_function([1,2,3], 2))
print(complex_recursive_function([4,5],3))


# 7 debug

def binary_search(nums, target):
    if not nums:
        return -1

    mid = len(nums) // 2

    if nums[mid] == target:
        return mid

    elif nums[mid] > target:
        return binary_search(nums[:mid], target)  

    else:
        result = binary_search(nums[mid+1:], target)
        return mid + 1 + result if result != -1 else -1

print(binary_search([1,2,3,4,5], 4))

# 2 Merge two sorted linked lists recursively

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    
    if l1.val < l2.val:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2

# Helper function to print linked list (for testing)
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Creating linked lists for testing
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

# Merging and printing the result
merged_list = merge_two_lists(l1, l2)
print_linked_list(merged_list)

# 1 Given a string, return True if it is a nesting of zero or more pairs of parentheses. Return Flase otherwise. A valid pair of parentheses is defined as ().

# Complete the 'is_nested' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING paren_s as parameter.
#

def is_nested_parens(paren_s):
    # Write your code here
    # Base case: an empty string is valid
    if not paren_s:
        return True

    if paren_s[0] == '(' and paren_s[-1] == ')': # check the substring
        return is_nested_parens(paren_s[1:-1])
    # If it doesn't match, it is not valid
    return False

# Test cases
print(is_nested_parens("(())"))  # Output: True
print(is_nested_parens("()"))    # Output: True
print(is_nested_parens(")("))    # Output: False
print(is_nested_parens("(()"))   # Output: False
print(is_nested_parens(""))      # Output: True