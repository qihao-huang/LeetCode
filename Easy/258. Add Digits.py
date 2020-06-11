# Runtime: 28 ms, faster than 84.14% of Python3 online submissions for Add Digits.
# Memory Usage: 13.8 MB, less than 51.56% of Python3 online submissions for Add Digits.

class Solution:
    def addDigits(self, num):
        if num == 0:
            return 0
        else:    
            return 1 + (num-1)%9

num = 38
ret = Solution().addDigits(num)
print(ret)