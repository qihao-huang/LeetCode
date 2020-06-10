# Return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

# Input: haystack = "hello", needle = "ll"
# Output: 2

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Runtime: 40 ms, faster than 26.83% of Python3 online submissions for Implement strStr().
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Implement strStr().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        if not needle in haystack:
            return -1
        else:
            for i in range(len(haystack)):
                if haystack[i:i+len(needle)] == needle:
                    return i

haystack = "hello"
needle = "ll"

# haystack = "aaaaa"
# needle = "bba"

ret = Solution().strStr(haystack, needle)
print(ret)