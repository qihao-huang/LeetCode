# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)

# help: https://blog.csdn.net/xinxin100011/article/details/81258144
# FIXME: [string]
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # math pattern or matrix way



s = "PAYPALISHIRING"
numRows = 4
ret = Solution().convert(s, numRows)
print(ret)

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Explanation:
# P1    A5    H9      N13
# A2 P4 L6 S8 I10 I12 G14
# Y3    I7    R11

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"

# Explanation:
# P1      I7         N13
# A2   L6 S8     I12 G14
# Y3 A5   H9  R11
# P4      I10

# Input: s = ABCDEFGHIGKLMNO numRows = 5
# Output: "AIBHJCGKODFLNEM"
# A1           I9
# B2        H8 J10             
# C3     G7    K11      O15
# D4  F6       L12  N14
# E5           M13

