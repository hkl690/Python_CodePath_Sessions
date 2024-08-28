"""
Session 1: Problem 2: Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that 
they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def twoSum(nums, target):
    
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def twoSumDict(nums, target):
    dict = {}
    
    for i, num in enumerate(nums):
        # If we see the counterpart in our hashmap(dict) then return the index of the counterpart and current index
        if num in dict:            
            return [dict[num], i]
        # Store the counterpart of the number we have seen and current index
        dict[target - num] = i
        

print(twoSum([2,7,11,15], 9))
print(twoSumDict([2,7,11,15], 9))
print(twoSum([2,7,11,15], 26))
print(twoSumDict([2,7,11,15], 26))
print(twoSum([3,2,4], 6))
print(twoSumDict([3,2,4], 6))
print(twoSum([3,3], 6))
print(twoSumDict([3,3], 6))