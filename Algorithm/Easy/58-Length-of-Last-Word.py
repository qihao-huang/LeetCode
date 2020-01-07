# Given a string s consists of upper/lower-case alphabets and 
# empty space characters ' ', return the length of last word 
# (last word means the last appearing word if we loop from left to right) in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a maximal substring consisting of non-space characters only.

# Input: "Hello World"
# Output: 5

# Runtime: 24 ms, faster than 84.84% of Python3 online submissions for Length of Last Word.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Length of Last Word.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ss = s.strip().split(" ")

        return len(ss[-1])
        

s = "Hello World"
ret = Solution().lengthOfLastWord(s)
print(ret)