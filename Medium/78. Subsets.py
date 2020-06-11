# Runtime: 24 ms, faster than 98.47% of Python3 online submissions for Subsets.
# Memory Usage: 13.9 MB, less than 81.71% of Python3 online submissions for Subsets.

class Solution:
    def subsets(self, nums):
        rst = [[]]
        for num in nums:
            for pos in rst[:]:
                x = pos[:]
                x.append(num)
                rst.append(x)

        return rst


nums = [1,2,3]
ret = Solution().subsets(nums)
print(ret)
