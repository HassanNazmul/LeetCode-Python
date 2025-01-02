# 35. Search Insert Position

nums = [1,3,5,6]
target = 5

# Linear Search and Insert
def searchInsert(nums, target):
    if target in nums:                        # Check if target exists in nums
        return nums.index(target)             # Return index if found
    else:
        nums.append(target)                   # Add target to nums
        nums.sort()                           # Sort nums in ascending order
        return nums.index(target)             # Return index of target

print(searchInsert(nums, target))             # Print result



# NOTES:
    # # To solve this problem, follow these steps:
        # 1. Use if statement to check if target exists in nums array
        # 2. If target exists, return its index using nums.index(target)
        # 3. If target doesn't exist, add target to nums array
        # 4. Sort nums array to maintain ascending order
        # 5. Return index of target after sorting using nums.index(target)

    # .index() method returns the index of the first occurrence of the specified value
    # .sort() method sorts the list ascending by default
    # .append() method adds an element to the end of the list
