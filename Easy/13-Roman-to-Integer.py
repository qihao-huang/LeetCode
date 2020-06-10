# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# Runtime: 48 ms, faster than 49.70% of Python3 online submissions for Roman to Integer.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Roman to Integer.

class Solution:
    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
    
    def romanToInt(self, s: str) -> int:
        sum_int = 0
        i = 0
        while True:
            if i > len(s)-1:
                break
            if i+1 <= len(s)-1:
                if self.roman_dict[s[i]] < self.roman_dict[s[i+1]]:
                    sum_int += (self.roman_dict[s[i+1]]-self.roman_dict[s[i]])
                    i += 2
                else:
                    sum_int += self.roman_dict[s[i]]
                    i += 1
            else:
                sum_int += self.roman_dict[s[i]]
                i += 1

        return sum_int

# s = "I" # 3
# s = "IV" # 4
# s = "IX" # 9
# s = "LVIII" # 58 L = 50, V= 5, III = 3.
s = "MCMXCIV" # 1994 M = 1000, CM = 900, XC = 90 and IV = 4.
ret = Solution().romanToInt(s)
out = str(ret)
print(out)
