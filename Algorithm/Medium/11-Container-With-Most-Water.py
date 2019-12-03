# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, 
# such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49 # 7*7

# Runtime: 128 ms, faster than 94.89% of Python3 online submissions for Container With Most Water.
# Memory Usage: 14.4 MB, less than 81.05% of Python3 online submissions for Container With Most Water.

class Solution:
    def maxArea(self, height) -> int:
        if len(height) == 2:
            return min(height)

        maxA = 0
        i = 0
        j = len(height)-1        
        while True:
            if i>=j:
                break

            i_height = height[i]
            j_height = height[j]

            area = (j-i)*(min(i_height, j_height))
            if area > maxA:
                maxA = area
            
            if i_height >= j_height:
                j -= 1
            else:
                i += 1
        
        return maxA
            

# height = [1, 1] # 1
# [1,8,6,2,5,4,8,3,7] # 47
height = [2,3,4,5,18,17,6] # 17
ret = Solution().maxArea(height)
print(height, ret)