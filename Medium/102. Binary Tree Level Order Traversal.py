# Runtime: 36 ms, faster than 57.53% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 13.9 MB, less than 93.45% of Python3 online submissions for Binary Tree Level Order Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode):

        res = []
        if root is None:
            return res
        
        from collections import deque

        que = deque([root])

        while len(que)!=0:
            lev = []
            thislevel = len(que)
            while thislevel != 0:
                head = que.popleft()
                if head.left is not None:
                    que.append(head.left)
                if head.right is not None:
                    que.append(head.right)
                
                lev.append(head.val)
                thislevel -= 1
            
            res.append(lev)

        return res


# [3,9,20,null,null,15,7]