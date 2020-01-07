# Given a string, determine if it is a palindrome, 
# considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, 
# we define empty string as valid palindrome.

# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: "race a car"
# Output: false

# Runtime: 52 ms, faster than 42.79% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 13.8 MB, less than 57.14% of Python3 online submissions for Valid Palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:        
        s = s.strip().lower()
        ss = [x for x in s if x.isalpha() or x.isnumeric()]

        if len(ss)==1 or len(ss)==0:
            return True

        for i in range(len(ss)):
            j = len(ss)-1-i
            if ss[i] == ss[j]:
                if i<j and i+1 != j-1:
                    continue
                else:
                    return True
            else:
                return False

# s = "A man, a plan, a canal: Panama" # True
# s = "race a car" # False
# s = ".,"
s = "0P"
ret = Solution().isPalindrome(s)
print(ret)