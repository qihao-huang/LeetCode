# Runtime: 20 ms, faster than 98.45% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 13.8 MB, less than 72.98% of Python3 online submissions for Invert Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # Edge 
        if not root:
            return 
        
        # Swap
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # Recursion
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return 
        return root

