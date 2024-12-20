# 26. Remove Duplicates from Sorted Array

nums = [0,0,1,1,1,2,2,3,3,4]

if len(nums) == 0:  # If the list is empty, return 0
    print(0)
else:
    i = 0   # Initialize a pointer at the beginning of the list
    for j in range(1, len(nums)):   # Iterate over the list starting from the second element
        if nums[j] != nums[i]:  # If the current element is different from the previous element
            i += 1  # Move the pointer to the next position
            nums[i] = nums[j]   # Update the value at the pointer position
    print(i + 1)    



# NOTES:
# - The list is assumed to be sorted in ascending order.
# - We use two pointers, i and j, to traverse the list.
# - The pointer i is used to keep track of the unique elements in the list.
# - The pointer j is used to iterate over the list.
# - When we encounter a new element, we increment i, update the value at position i, and continue.
# - The final length of the list is i + 1, as i is zero-based.