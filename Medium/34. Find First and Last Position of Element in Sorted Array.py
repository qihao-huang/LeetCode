# Runtime: 92 ms, faster than 15.84% of Python online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 14 MB, less than 66.41% of Python online submissions for Find First and Last Position of Element in Sorted Array.

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                res = [0,0]
                if nums[left]==target:
                    res[0] = left
                if nums[right]==target:
                    res[1] = right
                
                for i in range(mid,right+1):
                    if nums[i] != target:
                        res[1] = i-1
                        break
                
                for i in range(mid,left-1,-1):
                    if nums[i] != target:
                        res[0] = i+1
                        break

                return res

        return [-1,-1]

#  O(log n)

nums = [5,7,7,8,8,10]
target = 8
# Output: [3,4]

# nums = [5,7,7,8,8,10]
# target = 6
# Output: [-1,-1]

ret = Solution().searchRange(nums, target)
print(ret)