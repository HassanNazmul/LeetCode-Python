# 136. Single Number

# Brute Force
def singleNumber(nums):
    for i in range(len(nums)): # check each element in the list
        if nums.count(nums[i]) == 1:    # if the element appears only once
            return nums[i]  # return the element


# Using Hash Table
def singleNumberHash(nums):
    num_count = {}
    for i in nums:  # count the number of times each element appears in the list
        if i in num_count:  # if the element is already in the dictionary
            num_count[i] += 1   # increment the count
        else:
            num_count[i] = 1    # add the element to the dictionary

    for i in num_count: # check the dictionary
        if num_count[i] == 1:   # if the element appears only once
            return i    # return the element

# NOTES:
    # # To solve this problem, follow these steps:
        # 1. Create a dictionary to store the count of each element
        # 2. Iterate over the list and count the number of times each element appears
        # 3. Iterate over the dictionary and return the element that appears only once
    # # Built-in Functions:
        # .count() returns the number of times an element appears in a list
        # .items() returns a list of key-value pairs in a dictionary
        # .keys() returns a list of keys in a dictionary
        # .values() returns a list of values
