from unicodedata import numeric


def longestConsecutiveSequence(nums):
    longestStreak = 0
    dict = set(nums) # O(n)
    
    for num in dict: # O(n)
        # If current number has no previous number, then start counting from this number
        if num-1 not in dict: # O(1)
            currentNum = num
            currentStreak = 1
            # While the set contains currentNum + 1, increment currentNum and currentStreak
            while currentNum + 1 in dict: # O(1) per iteration, total O(n)
                currentNum += 1
                currentStreak += 1
            # After each while loop, check and set longestStreak
            longestStreak = max(longestStreak, currentStreak) # O(1)
            
    return longestStreak

print(longestConsecutiveSequence([100,4,200,1,3,2])) # Output: 4
print(longestConsecutiveSequence([0,3,7,2,5,8,4,6,0,1])) # Output: 9

# Assume N represents the number of items in the array.
# Time Complexity: O(N) because at the first glance, 
# the while loop inside the for loop may seem like the time complexity is O(n * n). 
# However, the while loop is only reached when the currentNum is the first of a subsequence, 
# the while loop can only run for n iterations throughout the entire runtime of the function. 
# So the runtime is actually O(n+n) = O(n).
# Space Complexity: O(N) because we store the numbers in a hashset.