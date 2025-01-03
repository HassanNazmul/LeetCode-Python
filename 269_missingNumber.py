# 268. Missing Number


# Brute Force
def missingNumber(nums):
    n = len(nums)   # length of the list
    for i in range(n+1):    # range of the list
        if i not in nums:   # if i is not in the list
            return i    # return i


# Gauss' Formula
def missingNumbers(nums):
    n = len(nums)   # length of the list
    expected_set = set(range(n+1))  # set of the range of the list
    num_set = set(nums) # set of the list
    return expected_set - num_set   # return the difference between the two sets
