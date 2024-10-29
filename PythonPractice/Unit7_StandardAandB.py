# Unit 7 Standard A
# 4 what is the time complexity

def mystery_function(n):
    if n == 0 or n ==1:
        return 1
    return n * mystery_function(n-1) # theirs said factorial(n-1) typo

# 5 What is the output
def mystery_function2(arr):
    if not arr:
        return 0
    return arr[0] + mystery_function2(arr[1:])

print(mystery_function2([1,2,3,4,5]))
print(mystery_function2([10,20,30]))


# 6 
from collections import deque
from turtle import right

def recursive_helper(queue):
    if not queue:
        return 0
    current = queue.popleft()
    return current + recursive_helper(queue)

def sum_with_queue(arr):
    queue = deque(arr)
    return recursive_helper(queue)

print(sum_with_queue([1,2,3,4,5]))

# 7 debug this code
import math
import os
import random
import re
import sys
import ast

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    return -1

# 1 compute power function
# given two integers, x and n, whree n is non-negative, write a function power() that recursively computes and return x^n

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

print(power(2,3))

# 2 bad product
# given a list of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.
# Return the smallest character in letters that is lexicographically greater (occurs later in the alphabet) than target. If such a character does not exist, return the first character in letters. Must have O(log n) time complexity.

def next_greatest_letter(letters, target):
    left, right = 0, len(letters) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

    # If left is out of bounds, wrap around to the first element
    return letters[left % len(letters)]

letters = ["c","f","j"]
target = "a" # ouput = "c"
print(next_greatest_letter(letters,target))

letters = ["x","x","y","y"]
target = "z" # output = "z" because there are no characters in letters that is lexicographically greater than 'z' so we return letters[0]
print(next_greatest_letter(letters,target))

# 3 first and last position of element in sorted array
# given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If the target is not found in the array, return [-1,-1]. Use O(log n) runtime complexity.

def search_range(nums, target):
    def find_left(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    def find_right(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    left_index = find_left(nums, target)
    right_index = find_right(nums, target)

    if left_index <= right_index and right_index < len(nums) and nums[left_index] == target and nums[right_index] == target:
        return [left_index, right_index]
    else:
        return [-1, -1]

nums = [5,7,7,8,8,10]
target = 8 # output = [3,4]
print(search_range(nums, target))

nums = [5,7,7,8,8,10]
target = 6
print(search_range(nums, target))

# 6
def recursive_helper2(index, stack, arr):
    if index == len(arr):
        return 0
    stack.append(arr[index])
    result = stack.pop() + recursive_helper2(index + 1, stack, arr)
    return result

def mystery_function3(arr):
    stack = []
    return recursive_helper2(0, stack, arr)

print(mystery_function3([10,20,30]))

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
        if result != -1:
            return mid + 1 + result
        else:
            return -1

# 2
# Complete the 'find_first_occurrence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY names
#  2. STRING val
#

def find_first_occurrence(names, val):
    # Write your code here
    left, right = 0, len(names) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        if names[mid] == val:
            result = mid
            right = mid - 1
        elif names[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
            
    return result


names = ["Alice", "Bob", "Charlie", "David"]
val = "Charlie" # output 2
print(find_first_occurrence(names, val))

names = ["Alice", "Bob", "Charlie", "David"]
val = "Cat" # output -1
print(find_first_occurrence(names, val))

# 3 unique element
# Given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Return the single element that appears only once. Run in O(log n) time and O(1) space.

def single_non_duplicate(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        # ensure mid is even
        if mid % 2 == 1:
            mid -= 1

        # check if the pair is broken
        if nums[mid] == nums[mid + 1]:
            left = mid + 2
        else:
            right = mid

    return nums[left]

# Test cases
nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
print(single_non_duplicate(nums))  # Output: 2

nums = [3, 3, 7, 7, 10, 11, 11]
print(single_non_duplicate(nums))  # Output: 10