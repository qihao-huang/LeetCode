# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/solution/

# 递归

# 左子树和右子树的最大深度 ll 和 rr，那么该二叉树的最大深度即为 max(l,r)+1
# 先递归计算出其左子树和右子树的最大深度，然后在 O(1)时间内计算出当前二叉树的最大深度。
# 递归在访问到空节点时退出。

# 时间复杂度：O(n)，其中 nn 为二叉树节点的个数。每个节点在递归中只被遍历一次。
# 空间复杂度：O(height)，height 表示二叉树的高度。递归函数需要栈空间，而栈空间取决于递归的深度，因此空间复杂度等价于二叉树的高度。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            l_height = self.maxDepth(root.left)
            r_height = self.maxDepth(root.right)

            return max(l_height, r_height) + 1

