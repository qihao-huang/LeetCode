# Runtime: 816 ms, faster than 30.26% of Python3 online submissions for Two Sum.
# Memory Usage: 13.8 MB, less than 75.81% of Python3 online submissions for Two Sum.

class Solution:
    def twoSum(self, nums, target):
        for i, i_value in enumerate(nums):
            j_value = target-i_value
            if  j_value in nums:
                j = nums.index(j_value)
                if i!=j:
                    return [i,j]