"""
Problem 1: Contains Duplicates
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""

def containsDuplicates(nums):
    dict = {}
    for num in nums:
        if num in dict:
            return True
        else:
            dict[num]=True
    return False

print(containsDuplicates([1,2,3,1]))
print(containsDuplicates([1,2,3,4]))
print(containsDuplicates([1,1,1,3,3,4,3,2,4,2]))