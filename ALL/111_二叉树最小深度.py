# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        min_depth = 1e9

        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.mindepth(root.right), min_depth)

        return min_depth + 1

# 时间复杂度：O(N)，其中 N 是树的节点数。对每个节点访问一次。

# 空间复杂度：O(H)，其中 H 是树的高度。空间复杂度主要取决于递归时栈空间的开销，最坏情况下，树呈现链状，空间复杂度为 O(N)。
# 平均情况下树的高度与节点数的对数正相关，空间复杂度为 O(logN)。

# Solution 2: 广度优先搜索

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        que = collections.deque([(root, 1)])
        while que:
            node, depth = que.popleft()
            if not node.left and not node.right:
                return depth
            
            if node.left:
                que.append((node.left, depth+1))
            
            if node.right:
                que.append((node.right, depth+1))

        return 0

# 时间复杂度：O(N)，其中 N 是树的节点数。对每个节点访问一次。
# 空间复杂度：O(N)，其中 N 是树的节点数。空间复杂度主要取决于队列的开销，队列中的元素个数不会超过树的节点数。
