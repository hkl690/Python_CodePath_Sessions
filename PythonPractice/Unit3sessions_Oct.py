
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

# 2 kth largest element in array, solve without sorting
def find_kth_largest(nums, k):
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]

nums = [3,2,1,5,6,4]
k = 2 # output 5 because 5 is the 2nd largest element
print(find_kth_largest(nums, k))
nums = [3,2,3,1,2,4,5,5,6]
k = 4 # output 4 is the 4th largest element since duplicates are counted
print(find_kth_largest(nums, k))

# 3 Longest subarray with absolute difference less than or equal to limit
# Given an array of integers "nums" and an integer "limit", return the size
# of the longest non-empty subarray such that the absolute difference 
# between any two elements of this subarray is less than or equal to "limit".

def longest_subarray(nums, limit):
    max_deque = deque()
    min_deque = deque()
    left = 0
    result = 0

    for right in range(len(nums)):
        while max_deque and nums[max_deque[-1]] <= nums[right]:
            max_deque.pop()
        while min_deque and nums[min_deque[-1]]>= nums[right]:
            min_deque.pop()

        max_deque.append(right)
        min_deque.append(right)

        while nums[max_deque[0]] - nums[min_deque[0]] > limit:
            left += 1
            if max_deque[0] < left:
                max_deque.popleft()
            if min_deque[0] < left:
                min_deque.popleft()

        result = max(result, right - left + 1)

    return result

print(longest_subarray([8, 2, 4, 7], 4))  # Output: 2
print(longest_subarray([10, 1, 2, 4, 7, 2], 5))  # Output: 4
print(longest_subarray([4, 2, 2, 2, 4, 4, 2, 2], 0))  # Output: 3

# Unit 3 Advanced B

# 4

def process_chars(elements):
    queue = deque()
    stack = []

    for element in elements:
        queue.append(element)

    while queue:
        item = queue.popleft()
        stack.append(item)

        if len(stack)  % 2 == 0 and queue:
            stack.pop()

    return list(stack)

print(process_chars(["a","b","c","d","e"]))
        
# 5
def mystery(nums, k):
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heapreplace(min_heap, num)

    return min_heap[0]

print(mystery([3,2,1,5,6,4],2))

# 6
def mystery_function(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        max_water = max(max_water, min(height[left], height[right]) * width)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

print(mystery_function([1,8,6,2,5,4,8,3,7])) # 49

# 7
def first_uniq_char(s):
    char_count = {}
    queue = deque()

    for i, char in enumerate(s):
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            queue.append(i)

    while queue:
        index = queue.popleft()
        if char_count[s[index]] == 1:
            return index
    return -1

# 1 return vowels of a string. Vowels are 'a', 'e', 'i', 'o', 'u' and can be both upper and lower cases, more than once

def reverse_vowels(s):
    
    vowels_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', "U"}
    s_vowels = [char for char in s if char in vowels_set]
    result = []

    for char in s:
        if char in vowels_set:
            result.append(s_vowels.pop())
        else:
            result.append(char)

    return ''.join(result)

s = "hello"
print(reverse_vowels(s)) # "holle"

s = "codepath"
print(reverse_vowels(s)) # "cadepoth"

# 2 reverse polish notation
def evalRPN(tokens):
    operator_set = {'+', '-', '*', '/'}
    stack = []

    for token in tokens:
        if token not in operator_set:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a/b))

    return stack[0]

tokens = ["2", "1", "+", "3", "*"] # output 9 because ((2 + 1) * 3 = 9)
print(evalRPN(tokens))
tokens = ["4", "13", "5", "/", "+"] # 6 because (4 + (13/5)) = 6
print(evalRPN(tokens))

# 3 kth smallest element in a matrix
# use a heap
def kthSmallest(matrix, k):
    flat_list = [element for row in matrix for element in row]

    heapq.heapify(flat_list)

    for _ in range(k-1):
        heapq.heappop(flat_list)

    return heapq.heappop(flat_list)

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8 # output 13 because the elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest is 13
print(kthSmallest(matrix, k))
matrix = [[-5]]
k = 1 # output -5
print(kthSmallest(matrix, k))