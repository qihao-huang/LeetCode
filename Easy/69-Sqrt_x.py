# Implement int sqrt(int x).
# Compute and return the square root of x, where x is guaranteed 
# to be a non-negative integer.
# Since the return type is an integer, the decimal digits are truncated and 
# only the integer part of the result is returned.

# Input: 4
# Output: 2

# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
#              the decimal part is truncated, 2 is returned.

# Runtime: 36 ms, faster than 53.16% of Python3 online submissions for Sqrt(x).
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Sqrt(x).

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        L = 0
        R = x
        
        while (L+1)<R:
            mid = (L+R)//2
            if mid**2 <= x < (mid+1)**2:
                return mid
            elif mid**2 > x:
                R = mid
            else:
                L = mid

        return L

# x = 8 # 2
x = 808836200 # 28440
ret = Solution().mySqrt(x)
print(ret)
