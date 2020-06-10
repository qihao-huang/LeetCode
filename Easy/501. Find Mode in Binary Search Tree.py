# Runtime: 64 ms, faster than 34.31% of Python3 online submissions for Find Mode in Binary Search Tree.
# Memory Usage: 17.8 MB, less than 50.62% of Python3 online submissions for Find Mode in Binary Search Tree.

# tree traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root):        
        result = []
        count = {}
        if (root):
            self.helper(root, count)
            maxval = max(count.values())
        else:
            maxval = 0
        
        for i in count:
            if count[i] == maxval:
                result.append(i)
        return result
        
    def helper(self, root, count):
        if count.has_key(root.val):
            count[root.val] += 1
        else:
            count[root.val] = 1
        
        if (root.left):
            self.helper(root.left, count)
        if (root.right):
            self.helper(root.right, count)
        
        return count

line = [1,"null",2,2]
root = stringToTreeNode(line)
ret = Solution().findMode(root)
out = integerListToString(ret)
print(out)
