# 21. Merge Two Sorted Lists

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

list1 = [1,2,4]
list2 = [1,3,4]

dummy = ListNode()  # Create a dummy node to hold the result
current = dummy     # Create a pointer to the dummy node

# Compare nodes in list1 and list2
while list1 and list2:
    if list1.val < list2.val:  # Compare the values of the two lists
        current.next = list1   # Assign the smaller node to the result list
        list1 = list1.next     # Move to the next node in list1
    else:
        current.next = list2   # Assign the smaller node to the result list
        list2 = list2.next     # Move to the next node in list2
    current = current.next     # Move the pointer in the result list

# Attach remaining nodes
if list1: 
    current.next = list1
if list2: 
    current.next = list2

return dummy.next  # Return the merged list (skip the dummy node)



# NOTES:
# - The dummy node is used to simplify the code
# - The current pointer is used to build the result list
# - The while loop compares the values of the nodes in list1 and list2
# - The smaller node is assigned to the result list
# - The pointer is moved to the next node in the result list
# - The remaining nodes are attached to the result list
# - The dummy node is skipped when returning the merged list