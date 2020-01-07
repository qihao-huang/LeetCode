# Example 1:
# Input: 1
# Output: "A"

# Example 2:
# Input: 28
# Output: "AB"

# Example 3:
# Input: 701
# Output: "ZY"

# 1 -> A
# 2 -> B
# 3 -> C
# ...
# 26 -> Z
# 27 -> AA
# 28 -> AB 
# ...

# Runtime: 24 ms, faster than 81.97% of Python3 online submissions for Excel Sheet Column Title.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Title.

class Solution:
    def convertToTitle(self, n: int) -> str:
        # chr(ord('A') + 3) = D
        # A B C D
        cvt_s = ""
        
        while n!=0 :
            res_n = (n-1) % 26 # (28-1)%26=1
            cvt_s = chr(ord('A') + res_n) + cvt_s
            n = (n-1)//26

        return cvt_s

n = 28
ret = Solution().convertToTitle(n)
print(ret)