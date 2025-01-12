# 217. Contains Duplicate


# Set Length Comparison
def containsDuplicate(nums):
    # Convert the list to a set to remove duplicates, then compare lengths
    return len(nums) != len(set(nums))  # return the comparison of the length of the list and the length of the set of the list

# Hash Set Method
def containsDuplicate1(nums):
    seen = set()  # Initialize an empty set to keep track of seen numbers
    for num in nums:
        if num in seen:  # If the number is already in the set, a duplicate is found
            return True
        seen.add(num)  # Add the number to the set
    return False  # No duplicates found

# Sorting Method
def containsDuplicate2(nums):
    nums.sort()  # Sort the list
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:  # Check if adjacent elements are the same
            return True
    return False  # No duplicates found

# NOTES:
    # - The Set Length Comparison method converts the list to a set and compares lengths.
    # - The Hash Set Method uses a set to track seen numbers and checks for duplicates.
    # - The Sorting Method sorts the list and checks for adjacent duplicates.
