# Determine whether an integer is a palindrome. 
# An integer is a palindrome when it reads the same backward as forward.

# Runtime: 48 ms, faster than 98.34% of Python3 online submissions for Palindrome Number.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Palindrome Number.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if s[0] == "-":
            return False
        if len(s) == 1:
            return True

        for i in range(len(s)):
            j = len(s)-1-i
            if s[i] == s[j]:
                if i<j and i+1 != j-1:
                    continue
                else:
                    return True
            else:
                return False

xx = [
    -10,
    -121,
    121,
    10,
    0,
    100
    ]

for x in xx:
    ret = Solution().isPalindrome(x)
    print(x, ret)