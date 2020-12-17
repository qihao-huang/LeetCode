# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 前序遍历：根结点 ---> 左子树 ---> 右子树
# 中序遍历：左子树---> 根结点 ---> 右子树
# 后序遍历：左子树 ---> 右子树 ---> 根结点
# 层次遍历：只需按层次遍历即可

# https://img-blog.csdn.net/20150204101904649?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvTXlfSm9icw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center

# 前序遍历：1  2  4  5  7  8  3  6 
# 中序遍历：4  2  7  5  8  1  3  6
# 后序遍历：4  7  8  5  2  6  3  1
# 层次遍历：1  2  3  4  5  6  7  8

# 递归：
# 时间复杂度：O(n)，其中 nn 为二叉树节点的个数。二叉树的遍历中每个节点会被访问一次且只会被访问一次。
# 空间复杂度：O(n)。空间复杂度取决于递归的栈深度，而栈深度在二叉树为一条链的情况下会达到 O(n) 的级别。
# 递归的时候隐式地维护了一个栈

# 栈：
# 迭代的时候需要显式地将这个栈模拟出来

# 1：递归：直接递归版本、针对不同题目通用递归版本（包括前序、中序、后序）
# 2：迭代：最常用版本（常用主要包括前序和层序，即【DFS和BFS】）、【前中后】序遍历通用版本（一个栈的空间）、【前中后层】序通用版本（双倍栈（队列）的空间）
# 3：莫里斯遍历：利用线索二叉树的特性进行遍历
# 4：N叉树的前序遍历

# 144. 二叉树的前序遍历
# 94. 二叉树的中序遍历
# 145. 二叉树的后序遍历
# 102. 二叉树的层序遍历
# 589. N叉树的前序遍历

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
