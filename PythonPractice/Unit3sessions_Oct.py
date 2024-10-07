
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
import enum
from hmac import new
from operator import is_
from os import remove

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


# import sys

# my_list = []
# print(sys.getsizeof(my_list))  # Initial size

# # Adding elements to the list
# for i in range(20):
#     my_list.append(i)
#     print(f"Length: {len(my_list)}, Size in bytes: {sys.getsizeof(my_list)}")


# 4
def mystery(nums):
    left = 0
    right = 0

    while right < len(nums):
        if nums[right] != 0:
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp
            left += 1
        right += 1
    return nums

nums = [0,0,1,2,0,3]
print(mystery(nums))

def process_numbers(nums):
    stack = [1]
    for num in nums:
        if num%2 == 0:
            stack.append(num)
        elif len(stack) > 0 and num % 2 != 0:
            stack.pop()
    return stack

nums = [2,3,4,5,6,7]
print(process_numbers(nums))

# 6
def process_strings(chars):
    queue = deque(["start", "middle", "end"])
    for char in chars:
        if char.isupper():
            queue.append(char)
        elif len(queue) > 0 and char.islower():
            queue.popleft()
    return list(queue)

chars = ['A', 'b', 'C', 'd', 'E', 'f']
print(process_strings(chars))

# 7 debug
def check_balanced(s):
    stack = []
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in matching_parentheses.values():
            stack.append(char)
        elif char in matching_parentheses:
            if stack and stack[-1] == matching_parentheses[char]:
                stack.pop()
            else:
                return False
        else:
            return False
                
    return not stack
s1 = "()"
s2 = "()[]{}"
s3 = "(]"
print(check_balanced(s1)) # True
print(check_balanced(s2)) # True
print(check_balanced(s3)) # False

def remove_duplicates(nums):
    if not nums:
        return 0

    j = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
                 
    # print(nums)
    return j + 1              

print(remove_duplicates([1,1,2,3]))

# 2 Intersection of Two Arrays (Two Pointer)
def intersection(nums1, nums2):
    if not nums1 or not nums2:
        return []

    result = []
    p1 = 0
    p2 = 0
    nums1.sort()
    nums2.sort()

    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] == nums2[p2]:
            if not result or result[-1] != nums1[p1]: # avoid duplicates
                result.append(nums1[p1])
            p1 += 1
            p2 += 1
        elif nums1[p1] < nums2[p2]:
            p1 += 1
        else:
            p2 += 1

    return result

nums1 = [1, 2, 2, 3]
nums2 = [2, 2, 3, 4]
print(intersection(nums1, nums2))  # Output: [2, 3]

# 3 Number of students unable to eat lunch (stacks, queues)
# circular sandwich = 0, square sandwich = 1
# sandwiches are placed in a stack. if the student at the front of the queue prefers
# the sandwich on top of the stack, they will take it and leave the queue. Otherwise
# they will leave it and go to the queue's end.This continues until none of the queue
# students want to take the top sandwich and are thus unable to eat. Return the number
# of students that are unable to eat.
def count_students_unable_to_eat(students, sandwiches):
    count_students_in_queue = 0
    queue = deque(students)
    stack = sandwiches

    while queue and count_students_in_queue < len(queue):
        if queue[0] == stack[0]:
            queue.popleft()
            stack.pop(0)
            count_students_in_queue = 0 # resetting
        else:
            queue.append(queue.popleft())
            count_students_in_queue += 1
    return count_students_in_queue

students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
print(count_students_unable_to_eat(students, sandwiches))  # Output: 0
students = [1, 1, 0, 0, 1]
sandwiches = [0, 1, 0, 1, 0]
print(count_students_unable_to_eat(students, sandwiches))  # Output: 1

# 4
def process_elements(elements):
    queue = deque()
    stack = []

    for element in elements:
        queue.append(element)

    while queue:
        item = queue.popleft()
        stack.append(item)

        if len(stack) % 2 == 0 and queue:
            stack.pop()
    return list(stack)

result = process_elements([1,2,3,4,5])
print("result is ",result)

# 5
import heapq
def mystery_function(lists):
    min_heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))

    result_list = []

    # extract-min and push the next element from the same list
    while min_heap:
        value, list_idx, element_idx = heapq.heappop(min_heap)
        result_list.append(value)
        next_idx = element_idx + 1
        if next_idx < len(lists[list_idx]):
            heapq.heappush(min_heap, (lists[list_idx][next_idx], list_idx, next_idx))

    return result_list

print("5: ",mystery_function([[1,3],[2,4]]))

# 6
def mystery(nums):
    if not nums:
        return 0

    left = 0

    for right in range(1, len(nums)):
        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]

    return left + 1

print("6: ",mystery([1,1,2,2,2,3,4,4,5]))

# 7
def check_balanced(s):
    stack = []
    matching_parenthesis = {')': '(', '}': '{', ']':'['}

    for char in s:
        if char in matching_parenthesis.values():
            stack.append(char)
            
        elif char in matching_parenthesis.keys():
            if not stack or stack[-1] != matching_parenthesis[char]:
                return False
            stack.pop()

    return not stack

print(check_balanced('{([])}'))
print(check_balanced('])}{(['))
print(check_balanced('])}'))
print(check_balanced("(){}[]"))  # True
print(check_balanced("([{}])"))  # True
print(check_balanced("(]"))      # False
print(check_balanced("({[)]"))   # False