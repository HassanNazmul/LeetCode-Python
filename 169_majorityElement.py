# 169. Majority Element

nums = [2,2,1,1,1,2,2]

# Approach 1: Brute Force
for i in range(len(nums)):  # Iterate through the list of numbers
    count = 0           # Initialize a counter
    for j in range(len(nums)):  # Iterate through the list of numbers again
        if nums[i] == nums[j]:  # If the current number is equal to the number in the inner loop
            count += 1        # Increment the counter
    if count > len(nums) // 2:  # If the counter is greater than half the length of the list
        print(nums[i])  # Print the number
        break
    # return nums[i]

# Approach 2: Hash Map
hash_map = {}  # Initialize an empty dictionary

for num in nums:  # Iterate through the list of numbers
    if num in hash_map:  # If the number is already in the dictionary
        hash_map[num] += 1  # Increment the value of the key
    else:  # If the number is not in the dictionary
        hash_map[num] = 1  # Add the number to the dictionary with a value of 1

for key, value in hash_map.items():  # Iterate through the key-value pairs in the dictionary
    if value > len(nums) // 2:  # If the value is greater than half the length of the list
        print(key)  # Print the key
        break

# Approach 3: Sorting
nums.sort()  # Sort the list of numbers
print(nums[len(nums) // 2])  # Print the number at the middle