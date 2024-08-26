from unicodedata import numeric


def longestConsecutiveSequence(nums):
    longestStreak = 0
    dict = set(nums)
    
    for num in dict:
        # If current number has no previous number, then start counting from this number
        if num-1 not in dict:
            currentNum = num
            currentStreak = 1
            # While the set contains currentNum + 1, increment currentNum and currentStreak
            while currentNum + 1 in dict:
                currentNum += 1
                currentStreak += 1
            # After each while loop, check and set longestStreak
            longestStreak = max(longestStreak, currentStreak)
            
    return longestStreak

print(longestConsecutiveSequence([100,4,200,1,3,2]))
print(longestConsecutiveSequence([0,3,7,2,5,8,4,6,0,1]))