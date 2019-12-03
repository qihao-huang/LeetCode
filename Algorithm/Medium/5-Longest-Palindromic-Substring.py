# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: "cbbd"
# Output: "bb"

# help: https://blog.csdn.net/qq_17550379/article/details/84022845
# help: https://blog.csdn.net/qq_17550379/article/details/84022674
# FIXME: [dynamic programming, string]
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # longest palindromic substring in s
        t = len(s)


        return 



s = "babad"
s = "cbbd"

ret = Solution().longestPalindrome(s)
print(ret)