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
