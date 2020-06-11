# Runtime: 40 ms, faster than 13.87% of Python3 online submissions for Unique Binary Search Trees.
# Memory Usage: 13.8 MB, less than 64.76% of Python3 online submissions for Unique Binary Search Trees.

# class Solution:
#     def numTrees(self, n):
#         res = 1
#         for i in range(n+1, 2*n+1):
#             res *= i/(i-n)

#         return round(res/(n+1))

# Runtime: 44 ms, faster than 10.84% of Python3 online submissions for Unique Binary Search Trees.
# Memory Usage: 13.8 MB, less than 54.81% of Python3 online submissions for Unique Binary Search Trees.

class Solution:
    def numTrees(self, n):
        res = [0]*(n+1)
        res[0] = 1

        for i in range(n+1):
            for k in range(i):
                res[i] += res[k]*res[i-1-k]
            
        return res[n]
        
n=7
ret = Solution().numTrees(n)
print(ret)


# 95. Unique Binary Search Trees II
# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3