# Given a string, find the length of the longest substring without repeating characters.

# Example 1:
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 

# Example 2:
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# TODO: needed improvement in Runtime
# Runtime: 64 ms, faster than 72.98% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Substring Without Repeating Characters.

# a smarter way use looping string and "in" and "index" of python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        curSubString = []

        for letter in s:
            if letter in curSubString:
                letterIndex = curSubString.index(letter)
                curSubString = curSubString[letterIndex+1:]
            
            # no matter letter is in curSubString or not
            # add letter to the end of curSubString
            curSubString.append(letter)
            maxLength = max(maxLength, len(curSubString))

        return maxLength

# TODO: brute force way, Time Limit Exceeded, not a good way
class Solution_1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if self.uniqueJudge(s): 
            return len(s)
        else:
            for i in range(len(s)-1):
                # from full size to small size, to get the longest first
                slideWinSize = len(s) - 1 - i
                for j in range(i+2):
                    if self.uniqueJudge(s[j:j+slideWinSize]):
                        return slideWinSize

    def uniqueJudge(self, subStr: str) -> bool:
        return True if len(set(subStr)) == len(subStr) else False