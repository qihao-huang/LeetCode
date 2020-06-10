# Runtime: 28 ms, faster than 85.49% of Python3 online submissions for Valid Boomerang.
# Memory Usage: 13.9 MB, less than 24.70% of Python3 online submissions for Valid Boomerang.

class Solution:
    def isBoomerang(self, points):
        p_1_x, p_1_y = points[0][0], points[0][1]
        p_2_x, p_2_y = points[1][0], points[1][1]
        p_3_x, p_3_y = points[2][0], points[2][1]

        if (p_1_x*p_2_y+p_2_x*p_3_y+p_3_x*p_1_y-p_1_x*p_3_y-p_2_x*p_1_y-p_3_x*p_2_y) == 0:
            return False
        else:
            return True

# |x1 y1 1|
# |x2 y2 1|
# |x3 y3 1|
# S=(x1y2+x2y3+x3y1-x1y3-x2y1-x3y2)/2


# points = [[1,1],[2,3],[3,2]]
points = [[1,1],[2,2],[3,3]]
ret = Solution().isBoomerang(points)
print(ret)