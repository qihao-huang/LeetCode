# Given an integer n, return the number of trailing zeroes in n!.

# Example 1:
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.

# Example 2:
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.

# Runtime: 20 ms, faster than 96.77% of Python3 online submissions for Factorial Trailing Zeroes.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Factorial Trailing Zeroes.

class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt=0
        while n>1:
            cnt += n//5
            n = n//5

        return cnt

# stupid approach, exceed time expectation 
# class Solution:
#     def trailingZeroes(self, n: int) -> int:
#         factorial = 1
#         while n>0:
#             factorial *= n
#             n -= 1

#         return len(str(factorial)) - len(str(factorial).rstrip("0"))

# 7756*7755*7754*....*5*4*3*2*1
# the number of 2 is far more than number of 5
# so, we only have to count the number of 5
n = 7756 # 1937
ret = Solution().trailingZeroes(n)
print(ret)