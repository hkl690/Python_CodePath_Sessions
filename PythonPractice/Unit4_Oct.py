#prompt = input('Please enter a word: ')
#print(prompt)


# Unit 4 Standard 1
# Problem 1: NFT Name Extractor
# You're curating a large collection of NFTs for a digital art gallery, and your first task is to extract the names of these NFTs from a given list of dictionaries. Each dictionary in the list represents an NFT, and contains information such as the name, creator, and current value.
# Write the extract_nft_names() function, which takes in this list and returns a list of all NFT names.

from imp import find_module
from itertools import filterfalse
import string


def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names

# Example usage:
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))

# Problem 2: NFT Collection Review
def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
]

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

nft_collection_3 = []

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))

# Problem 3: Identify Popular Creators
# You have been tasked with identifying the most popular NFT creators in your collection. A creator is considered "popular" if they have created more than one NFT in the collection.
# Write the identify_popular_creators() function, which takes a list of NFTs and returns a list of the names of popular creators.

def identify_popular_creators(nft_collection):
    creator_count = {}

    for nft in nft_collection:
        creator = nft["creator"]
        if creator in creator_count:
            creator_count[creator] += 1
        else:
            creator_count[creator] = 1

    pop_creators = [creator for creator, count in creator_count.items() if count > 1]
    return pop_creators

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3)) # empty

# Unit 4 Standard A

# 4 Time complexity question
def complex_function(nums):
    total = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] < nums[j]:
                total += nums[j] - nums[i]
    return total

# 5 Which of the following data structures/algorithmic techniques would be most appropriate for implementing this function?

# The function find_mode() takes in a list of elements lst and returns the mode of the list. If there are multiple modes, it returns them all as a list. If there is a single mode it returns the mode as a single value. The mode is the element that occurs most often in the list.

# Example usage:
# nums1=[1,2,2,3,4]
# print(find_mode(nums1)) # output 2

# nums2 = [1,2,2,3,3,4]
# print(find_mode(nums2)) # output [2,3]

# nums3 = [1,2,3,4,5]
# print(find_mode(nums3)) # output [1,2,3,4,5]

# answer: (?) frequency map

# 6
def process_numbers(nums, threshold):
    stack = []
    for num in nums:
        if num < threshold:
            stack.append(num)
        elif num <= 10 and stack:
            stack.pop()
    return stack

print(process_numbers([3,5,1,9,6,15], 8)) # [3,5,6]

# 7 find the bug
def is_anagram(s, t):
    if len(s) != len(t):
        return False

    s_freq = {}
    t_freq = {}

    for char in s:
        if char in s_freq:
            s_freq[char] += 1
        else:
            s_freq[char] = 1

    for char in t:
        if char in t_freq:
            t_freq[char] += 1
        else:
            t_freq[char] = 1

    return s_freq == t_freq

print(is_anagram("car", "rac"))
print(is_anagram("cat", "rac"))

# 2 Check if array is sorted and rotated

# given an array nums, return True if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return False.

# There may be duplicates in the original array. 
def is_sorted_rotated(nums):
    count = 0
    n = len(nums)

    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            count += 1
        if count > 1:
            return False

    return True

nums = [3,4,5,1,2]
print(is_sorted_rotated(nums)) # True. You can rotate the array by x = 3 positions to begin on the element of value 3: [3,4,5,1,2]

nums = [2,1,3,4]
print(is_sorted_rotated(nums)) # False. there is no sorted array once rotated that can make nums

nums = [1,2,3]
print(is_sorted_rotated(nums)) # True. You can rotate the array by x = 0 positions to make nums.

# 1 Move Zeroes
# Given a 0-indexed integer array nums of length n and an integer target, write a function count_pairs (i, j) where 0 <= i < j < n, and nums[i] + nums[j] < target

def count_pairs(nums, target):
    count = 0
    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] < target:
                count += 1
                
    return count
nums = [-1,1,2,3,1]
target = 2 # output 3, there are 3 pairs of indices that satisfy the conditions in the statement: (0,1) since 0<1 and nums[0] + nums[1] = 0 < target. (0,2) since 0<2 and nums[0] + nums[2] = 1 < target, (0,4) since 0<4 and nums[0] + nums[4] = 0 < target. Note that (0,3) is not counted since nums[0] + nums[3] is not strictly less than the target.
print(count_pairs(nums, target))

# 3 Subarray sum equals k
# given an array of integers nums and integer k, return the total number of continuous subarrays whose sums equals to k

def subarray_sum(nums, k):
    count = 0
    n = len(nums)

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum == k:
                count += 1
    return count

nums = [1, 2, 3]
k = 3
print(subarray_sum(nums, k))
