# 88. Merge Sorted Array

nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3

# First, clear the extra zeros at the end of nums1
nums1[m:] = []  # Removes placeholders beyond the first m elements

# Extend nums1 with nums2
nums1.extend(nums2[:n])

# Sort nums1 to make it non-decreasing
nums1.sort()