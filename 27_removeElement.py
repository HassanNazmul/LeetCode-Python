# 27. Remove Element

nums = [3, 2, 2, 3]
val = 3

for i in range(len(nums) - 1, -1, -1):  # Iterate from the end of the list to the beginning
    if nums[i] == val:
        nums.pop(i)  # Remove the element if it equals val
print(len(nums))  # Return the updated length of the list



# NOTES:
# - The for loop iterates over the indices of the list in reverse order.
# - The list.pop() method removes the element at the specified index.
# - By iterating in reverse order, we avoid the issue of skipping elements when removing them from the list.
# -  - 1, -1, -1 is a common pattern for iterating over a list in reverse order.
# - reversed(range(len(nums))) can also be used to iterate over the indices in reverse order.