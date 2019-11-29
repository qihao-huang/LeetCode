# Assume we are dealing with an environment which could only store integers 
# within the 32-bit signed integer range: [−2^31,  2^31−1]. 
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

# Runtime: 36 ms, faster than 70.93% of Python3 online submissions for Reverse Integer.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Reverse Integer.

class Solution:
    def reverse(self, x: int) -> int:
        # x = 0 # edge cases
        if x == 0:
            return 0
        minus = False
        # x = -123 # -321
        if x < 0:
            minus = True 
            x = -x
        str_x = str(x)
        rev_x = ""

        # x = 901000 # edge cases
        nonZeroPos = float("inf")
        for i in range(len(str_x)):
            dig = str_x[-(i+1)]
            if dig == "0":
                continue
            else:
                nonZeroPos = i
                break

        for i in range(len(str_x)):
            dig = str_x[-(i+1)]
            # x = 120 # 21
            if dig == "0":
                # x = 901000 # edge cases
                if i >= nonZeroPos:
                    rev_x += dig
                else:
                    continue
            else:
                rev_x += dig

        if minus:
            x = -int(rev_x) 
        else:
            x = int(rev_x)

        # overflows checking
        # x > 2^31-1 or x < -2^31
        if x > 2147483647 or x < -2147483648:
            return 0
        else:
            return x

# Given a 32-bit signed integer, reverse digits of an integer.
# x = 123 # 321
# x = -123 # -321
# x = 120 # 21
# x = -4294967296
# x = 0 # edge cases
# x = 901000 # edge cases
ret = Solution().reverse(x)
print(ret)