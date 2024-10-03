
def mystery(nums):
    left = len(nums) - 1
    right = len(nums) - 1

    while right >= 0:
        if nums[right] != 0:
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp
            left -= 1
        right -= 1
    return nums

nums = [0,0,11,2,0,3]
print(mystery(nums))

def process_strings(chars):
    stack = ["start"]
    for char in chars:
        if char.isupper():
            stack.append(char)
        elif stack and char.islower():
            stack.pop()
    return stack

chars = ['A', 'b', 'c', 'D', 'E', 'f']
print(process_strings(chars))

from collections import deque
from operator import is_

def process_numbers(nums):
    queue = deque([10, 20, 30])
    for num in nums:
        if num %2 == 0:
            queue.append(num)
        elif queue and num %2 != 0:
            queue.popleft()
    return list(queue)

nums = [2,3,4,5,6,7]
print(process_numbers(nums))

def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        left += 1
        right -= 1

        if s[left].lower() != s[right].lower():
            return False

    return True

s = "amanalanacanalPanama"
print(is_palindrome(s))

s = "abbd"
print(is_palindrome(s))

# 3 Two Sum Sorted (Two Pointer Question)
# You are given a 1-indexed array of integers, numbers, which is already sorted in non-decreasing
# order. Find two distinct numbers in the array that sum up to a given target. Return the
# indices of these two numbers (1-based) as an array[index1, index2]. Return nothing if no pair exists. Each element can only be used once. The solution must run with constant extra space.

def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

numbers = [2,7,11,15]
target = 9
print(two_sum(numbers, target)) # [1, 2] since numbers[1] + numbers[2] = 9 and are 1-based

# 1 Valid Parenthesis (Stack question)
# Given a string containing just the '(',')', '{','}','[',']', determine if the input string is valid.
def is_valid(s):
    stack = []
    valid_chars = {'(':')', '{':'}', '[':']'}

    for char in s:
        if char in valid_chars:
            stack.append(char)
        elif len(stack) > 0 and char == valid_chars[stack[-1]]:
            stack.pop()
        else:
            return False
    return not stack # returns True if the stack is empty, and False if stack is not empty
    # In Python, an empty list is considered False, and a non-empty list is considered True. Therefore, not stack will be True if the stack is empty and False if the stack is not empty.
    # same as: return len(stack) == 0
    # or same as: if len(stack) == 0:
    #                   return True
    #             else:
    #                   return False


s1 = "()"
s2 = "()[]{}"
s3 = "(]"
print(is_valid(s1)) # True
print(is_valid(s2)) # True
print(is_valid(s3)) # False

# 2 First Non-Repeating Character (Queue question)
# Given a string s, find the first non-repeating character in it and return its index.
# If it does not exist, return -1.

from collections import deque

def first_non_repeating_character(s):
    queue = deque()
    counts = {}

    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
        queue.append(char)

    for char in queue:
        if counts[char] == 1:
            print(queue, counts)
            return s.index(char)

    return -1

s = "leetcode"
print(first_non_repeating_character(s)) # 0
s = "likeleetcode"
print(first_non_repeating_character(s)) # 1
s = "aabb"
print(first_non_repeating_character(s)) # -1