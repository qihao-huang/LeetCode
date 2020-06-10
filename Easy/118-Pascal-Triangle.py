# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

# Input: 5
# Output:
# [
#      [1],          0
#     [1,1],        0 1
#    [1,2,1],      0 1 2 
#   [1,3,3,1],    0 1 2 3
#  [1,4,6,4,1]   0 1 2 3 4
# ]

# Runtime: 28 ms, faster than 63.39% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Pascal's Triangle.

class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []

        pascal_array = []
        pascal_array.append([1])

        for i in range(1,numRows):
            tmp_array = [1]*(i+1)
            for j in range(1,i):
                tmp_array[j] = pascal_array[i-1][j-1]+pascal_array[i-1][j]
            
            pascal_array.append(tmp_array)

        return pascal_array

numRows = 5
ret = Solution().generate(numRows)
print(ret)