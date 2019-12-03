# Given an input string (s) and a pattern (p), 
# implement regular expression matching with support for '.' and '*'.

# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.

# False
# s = "mississippi"
# p = "mis*is*p*."

# True
# s = "aab"
# p = "c*a*b"

# True
# s = "ab"
# p = ".*"

# True
# s = "aa"
# p = "a*"

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # False
        # s = "aa"
        # p = "a"
        if (not "." in p) and (not "*" in p):
            if s == p:
                return True
            else:
                return False
        
        uni_s = list(set(s))


