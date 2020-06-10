# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.

# Runtime: 92 ms, faster than 95.89% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Median of Two Sorted Arrays.

# FIXME: [binary search]
# solution video https://www.youtube.com/watch?v=LPFhl65R7ww
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # normal cases with time complexity O(log(min(nums1,nums2))
        # to make sure x_list is always the minor length one
        if len(nums1) <= len(nums2):
            x_list, y_list = nums1, nums2
        else:
            x_list, y_list = nums2, nums1

        m = len(x_list)
        n = len(y_list)
        sum_x_y = (m+n+1)//2
        # m+n is odd or even, m <= n
        odd = False if (m+n)%2 == 0 else True

        start_search_x = 0
        end_search_x = m

        while True:
            # parition_x: numbers of x in the left part
            partition_x = (start_search_x+end_search_x)//2
            # parition_y: numbers of y in the left part
            partition_y = sum_x_y - partition_x

            # e.g. x_list = [1,2,3,4], partition_x = 2
            leftX = x_list[:partition_x] # [1,2]
            rightX = x_list[partition_x:] # [3,4]

            leftY = y_list[:partition_y]
            rightY = y_list[partition_y:]

            # edge cases, empty partition
            # ---------------------
            # {-INF} | all X
            # left Y | Right Y
            # ---------------------
            # all X  | {+INF}
            # left Y | Right Y
            # ---------------------
            # left X | right X
            # {-INF} | all Y
            # ---------------------
            # left X | right X
            # all Y  | {+INF}
            # ---------------------

            if len(leftX) == 0:
                leftX = [-float("inf")]
            if len(rightX) == 0:
                rightX = [float("inf")]
            if len(leftY) == 0:
                leftY = [-float("inf")]
            if len(rightY) == 0:
                rightY = [float("inf")]

            maxLeftX = leftX[-1]
            maxLeftY = leftY[-1]
            minRightX = rightX[0]
            minRightY = rightY[0]
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if odd:
                    return max(maxLeftX, maxLeftY)
                else:
                    return (max(maxLeftX, maxLeftY)+min(minRightX, minRightY))/2
            elif maxLeftX > minRightY:
                end_search_x = partition_x - 1
            elif maxLeftY > minRightX:
                start_search_x = partition_x + 1


# nums1 = [1, 3, 8, 9, 15]
# nums2 = [7, 11, 18, 19, 21, 25]

# nums1 = [23, 26, 31, 35]
# nums2 = [3, 5, 7, 9, 11, 16]

# nums1 = [1, 3]
# nums2 = [2]

nums1 = []
nums2 = [1]

ret = Solution().findMedianSortedArrays(nums1, nums2)
print(ret)