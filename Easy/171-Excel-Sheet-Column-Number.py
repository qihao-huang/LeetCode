# Runtime: 20 ms, faster than 98.86% of Python3 online submissions for Excel Sheet Column Number.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Number.

class Solution:
    def titleToNumber(self, s: str) -> int:
        # ord('A')-64 # 1
        # ord('Z')-64 # 26
        cur_int = 0
        cvt = 0
        for i in range(len(s)):
            cur_int = (ord(s[i])-64)*(26**(len(s)-i-1))
            cvt += cur_int

        return cvt

# Example 1:
# Input: "A"
# Output: 1

# Example 2:
# Input: "AB"
# Output: 28

# Example 3:
# Input: "ZY"
# Output: 701

s = "AB"
ret = Solution().titleToNumber(s)
print(ret)

# 168-Excel-Sheet-Column-Title
# class Solution:
#     def convertToTitle(self, n: int) -> str:
#         # chr(ord('A') + 3) = D
#         # A B C D
#         cvt_s = ""
        
#         while n!=0 :
#             res_n = (n-1) % 26 # (28-1)%26=1
#             cvt_s = chr(ord('A') + res_n) + cvt_s
#             n = (n-1)//26

#         return cvt_s

# n = 28
# ret = Solution().convertToTitle(n)
# print(ret)