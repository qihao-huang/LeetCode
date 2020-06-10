# Definition for a binary tree node.

# depth-first-search, breadth-first-search, tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        

#     1
#    / \
#   2   2
#    \   \
#    3    3
# [1,2,2,null,3,null,3]

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
[1,2,2,3,4,4,3]