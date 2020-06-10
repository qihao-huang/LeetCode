# Given a non-empty array of integers, 
# every element appears twice except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. 
# Could you implement it without using extra memory

# Example 1:
# Input: [2,2,1]
# Output: 1

# Example 2:
# Input: [4,1,2,1,2]
# Output: 4

# Runtime: 88 ms, faster than 64.58% of Python3 online submissions for Single Number.
# Memory Usage: 15.2 MB, less than 13.12% of Python3 online submissions for Single Number.

class Solution:
    def singleNumber(self, nums):
        import collections
        counts = collections.Counter(nums)

        return min(counts.keys(), key=counts.get)

# nums = [2,2,1] # 1
nums = [4,1,2,1,2] # 4
ret = Solution().singleNumber(nums)
print(ret)