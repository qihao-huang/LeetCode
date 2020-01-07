# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Example 1:
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

# Approach #2 Using Extra Array [Accepted]

# We use an extra array in which we place every element of the array at its correct position 
# i.e. the number at index ii in the original array is placed 
# at the index (i+k)%(length of array)(i+k). Then, we copy the new array to the original one.

# Runtime: 80 ms, faster than 24.72% of Python3 online submissions for Rotate Array.
# Memory Usage: 14.1 MB, less than 5.09% of Python3 online submissions for Rotate Array.

class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        tmp = [1]*len(nums)
        for i in range(len(nums)):
            tmp[(i + k) % len(nums)] = nums[i]

        for i in range(len(tmp)):
            nums[i] = tmp[i]


# Time Limit Exceeded
# class Solution:
#     def rotate(self, nums, k) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(k):
#             tmp = nums[-1]
#             for j in range(1,len(nums)):
#                 nums[len(nums)-j] = nums[len(nums)-j-1] 
            
#             nums[0] = tmp

# [5,6,7,1,2,3,4]
# nums = [1,2,3,4,5,6,7]
# k = 3

# [3,99,-1,-100]
nums = [-1,-100,3,99]
k = 2

ret = Solution().rotate(nums, k)
print(nums)