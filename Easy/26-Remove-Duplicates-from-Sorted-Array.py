# Given a sorted array nums, remove the duplicates in-place such that 
# each element appear only once and return the new length.

# Do not allocate extra space for another array, 
# you must do this by modifying the input array in-place with O(1) extra memory.

# Runtime: 84 ms, faster than 76.78% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 14.5 MB, less than 96.72% of Python3 online submissions for Remove Duplicates from Sorted Array.

class Solution:
    def removeDuplicates(self, nums) -> int:
        # two pointers, slow i and fast j
        i = 0
        for j in range(len(nums)-1):
            # print("nums[j+1]: ", nums[j+1])
            # print("nums[i]: ", nums[i])
            if nums[j+1] != nums[i]:
                i += 1
                nums[i] = nums[j+1]
        
        return i+1

nums = [0,0,1,1,1,2,2,3,3,4] # 5
# nums = [1,1,2] # 3
ret = Solution().removeDuplicates(nums)
print(ret)