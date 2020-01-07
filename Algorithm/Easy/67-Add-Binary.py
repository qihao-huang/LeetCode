# Given two binary strings, return their sum (also a binary string).
# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# Runtime: 32 ms, faster than 59.98% of Python3 online submissions for Add Binary.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Add Binary.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        sum_ab = ""
        if len(a) > len(b):
            a,b = b,a
        
        a = a.zfill(len(b))

        for k in range(len(a)):
            idx = len(a)-k-1
            tmp = int(a[idx])+int(b[idx])+carry
            # 0+0/0+1/1+0/1+1 + carry
            if tmp == 3:
                add_tmp = 1
                carry = 1
            elif tmp == 2:
                add_tmp = 0
                carry = 1
            elif tmp == 1:
                add_tmp = 1
                carry = 0
            elif tmp == 0:
                add_tmp = 0
                carry = 0
        
            sum_ab = str(add_tmp) + sum_ab

        if carry!=0:
            sum_ab = str(carry) + sum_ab

        return sum_ab

# a = "1010"
# b = "1011"
# Output: "10101"

a = "11"
b = "1"
# Output: "100"

ret = Solution().addBinary(a,b)
print(ret)