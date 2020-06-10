# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same 
# if they are structurally identical and the nodes have the same value.

# depth-first-search, tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


# Input:     1         1
#           / \       / \
#          2   3     2   3
s1 = [1,2,3]
s2 = [1,2,3]

# Input:     1         1
#           /           \
#          2             2
# s1 = [1,2]
# s2 = [1,null,2]

# Input:     1         1
#           / \       / \
#          2   1     1   2
# s1 = [1,2,1]
# s2 = [1,1,2]

p = stringToTreeNode(s1)
q = stringToTreeNode(s2)
ret = Solution().isSameTree(p, q)
print(ret)