# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

# Note that the row index starts from 0.
# TODO: Could you optimize your algorithm to use only O(k) extra space?

# Input: 3
# Output: [1,3,3,1]

# Runtime: 24 ms, faster than 88.56% of Python3 online submissions for Pascal's Triangle II.
# Memory Usage: 12.9 MB, less than 96.15% of Python3 online submissions for Pascal's Triangle II.

class Solution:
    def getRow(self, rowIndex):
        numRows = rowIndex+1

        if numRows == 0:
            return []

        pascal_array = []
        pascal_array.append([1])

        for i in range(1,numRows):
            tmp_array = [1]*(i+1)
            for j in range(1,i):
                tmp_array[j] = pascal_array[i-1][j-1]+pascal_array[i-1][j]
            
            pascal_array.append(tmp_array)

        return pascal_array[rowIndex]

rowIndex = 3
ret = Solution().getRow(rowIndex)
print(ret)