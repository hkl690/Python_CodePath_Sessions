
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