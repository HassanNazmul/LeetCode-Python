# 108. Convert Sorted Array to Binary Search Tree

# Dynamic Programming Solution
def sortedArrayToBST(self, nums):
    """
    Convert a sorted array into a height-balanced binary search tree.
    A height-balanced binary tree is a binary tree in which the depth of the two subtrees 
    of every node never differs by more than one.
    
    Args:
        nums: List[int], sorted array in ascending order
        
    Returns:
        TreeNode: Root of the constructed BST
    """
    # Base case: if array is empty, return None
    if not nums:
        return None
        
    # Find middle element to make it root
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    
    # Recursively construct left subtree using left half of array
    root.left = self.sortedArrayToBST(nums[:mid])
    
    # Recursively construct right subtree using right half of array
    root.right = self.sortedArrayToBST(nums[mid+1:])
    
    return root
