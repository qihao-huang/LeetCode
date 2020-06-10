# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)

# Runtime: 48 ms, faster than 98.61% of Python3 online submissions for ZigZag Conversion.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for ZigZag Conversion.

# help: https://blog.csdn.net/xinxin100011/article/details/81258144
# FIXME: [string]
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows_num = min(numRows, len(s))

        rows = ['']*rows_num # ['', '', '']

        cur_row = 0
        go_down = False
        for x in s:
            rows[cur_row] += x
            if cur_row == 0 or cur_row == numRows - 1:
                go_down = not go_down
                
            if go_down:
                cur_row += 1
            else:
                cur_row -= 1

        return ''.join(rows)

        # >>> str = '-'
        # >>> seq = ('b','o','o','k')
        # >>> print str.join(seq)
        # >>> b-o-o-k

s = "PAYPALISHIRING"
numRows = 3
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

