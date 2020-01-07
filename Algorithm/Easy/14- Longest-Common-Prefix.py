# All given inputs are in lowercase letters a-z.

# Input: ["dog","racecar","car"]
# Output: ""

# Input: ["flower","flow","flight"]
# Output: "fl"

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""

        # sorting
        s1 = min(strs)
        s2 = max(strs)
        
        # print(s1)
        # print(s2)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]

        return s1

# strs = ["dog", "racecar", "car"]
strs = ["flow", "flower", "flight"]
ret = Solution().longestCommonPrefix(strs)
out = str(ret)
print(out)