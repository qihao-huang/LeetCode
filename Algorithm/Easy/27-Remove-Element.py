# Given an array nums and a value val, 
# remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, 
# you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. 
# It doesn't matter what you leave beyond the new length.

# Given nums = [0,1,2,2,3,0,4,2], val = 2,
# Your function should return length = 5, 
# with the first five elements of nums containing 0, 1, 3, 0, and 4.
# Note that the order of those five elements can be arbitrary.
# It doesn't matter what values are set beyond the returned length.

# Runtime: 32 ms, faster than 55.33% of Python3 online submissions for Remove Element.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Remove Element.

class Solution:
    def removeElement(self, nums, val) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            
        return k


# 2
# nums = [3,2,2,3]
# val = 3 

# 5
nums = [0,1,2,2,3,0,4,2]
val = 2

ret = Solution().removeElement(nums, val)
print(ret)
