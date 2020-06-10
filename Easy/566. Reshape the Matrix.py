# Runtime: 124 ms, faster than 20.62% of Python3 online submissions for Reshape the Matrix.
# Memory Usage: 14.7 MB, less than 73.37% of Python3 online submissions for Reshape the Matrix.

class Solution:
    def matrixReshape(self, nums, r, c):
        mat = [x for row in nums for x in row]
        if r*c == len(mat):
            return [mat[i*c: (i+1)*c] for i in range(r)]
        else:
            return nums

nums = [[1,2], [3,4]]
r = 1
c = 4
ret = Solution().matrixReshape(nums,r,c)
print(ret)