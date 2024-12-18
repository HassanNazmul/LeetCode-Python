# 189. Rotate Array

nums = [1,2,3,4,5,6,7]
k = 3

# nums = (nums[-k:] + nums[:-k])
# print(nums)


n = len(nums)
k = k % n  # Handle cases where k > n

# Step 1: Reverse the entire list
nums.reverse()
print(nums)

# Step 2: Reverse the first k elements
nums[:k] = reversed(nums[:k])
print(nums)

# Step 3: Reverse the remaining elements
nums[k:] = reversed(nums[k:])
print(nums)



# NOTES:
# - nums[:k] is a slice of the list from the beginning to k
# - nums[k:] is a slice of the list from k to the end
# - reversed() is a built-in function that returns an iterator that produces the elements of the object in reverse order
# - reversed() is used to reverse the elements of the list in place
