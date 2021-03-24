# https://leetcode-cn.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 如果是二叉搜索树，那么中序遍历后得到的一定是升序
        # 中序遍历：先遍历左子树，再遍历根节点，最后遍历右子树。
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()

            if root.val <= inorder:
                return False
            
            inorder = root.val
            root = root.right
        
        return True
        