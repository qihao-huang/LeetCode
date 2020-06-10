# Implement atoi which converts a string to an integer.

# 1. discard as many whitespace characters as necessary 
# until the first non-whitespace character is found

# 2. starting from this character, takes an optional 
# initial plus or minus sign followed by as many numerical digits as possible

# 3. interprets them as a numerical value.

# The string can contain additional characters after those 
# that form the integral number, which are ignored and 
# have no effect on the behavior of this function.

# The first non-whitespace character is 'w', which is not a numerical 
# digit or a +/- sign. Therefore no valid conversion could be performed.
# Input: "words and 987"
# Output: 0

# Runtime: 24 ms, faster than 99.14% of Python3 online submissions for String to Integer (atoi).
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for String to Integer (atoi).

# FIXME: [string, corner cases]

class Solution:
    def myAtoi(self, s: str) -> int:
        ext_num = 0

        s = s.strip()

        if len(s)==0:
            return 0

        if not(s[0].isdigit() or s[0]=="+" or s[0]=="-"):
            return 0
        
        if s[0].isdigit():
            non_digit_t = 0
            for t, letter in enumerate(s):
                if not letter.isdigit():
                    non_digit_t = t
                    break

            if non_digit_t == 0:
                ext_num = int(s)
            else:
                ext_num = int(s[0:non_digit_t])
                
        elif s[0]=="+" or s[0]=="-":
            if s[0]=="+":
                coef = 1
            elif s[0]=="-":
                coef = -1

            sub_str = s[1:]
            if len(sub_str) == 0:
                return 0
            if not sub_str[0].isdigit():
                return 0
            non_digit_t = 0
            for t, letter in enumerate(sub_str):
                if not letter.isdigit():
                    non_digit_t = t
                    break

            if non_digit_t == 0:
                ext_num = coef*int(sub_str)
            else:
                ext_num = coef*int(sub_str[0:non_digit_t])

        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        if ext_num < INT_MIN:
            return INT_MIN
        elif ext_num > INT_MAX:
            return INT_MAX
        else:
            return ext_num

test_cases = [
    "+-2", # 0
    "+", # 0
    "", # 0
    "42",
    "123-", # 123
    "4193 with words", # 4193
    "3.14159", # 3
    "0.314", # 0
    "-13+8", # -13
    "  +b12102370352",
    "-5-", # -5
    "-   234", # -0
    "   -42", # -42
    "words and 987", # 0
    "-91283472332", # -2147483648
    "+1", # 1
    "  -0012a42", # -12
    ".1", # 0
]

for test in test_cases:
    ret = Solution().myAtoi(test)
    print("test with: \"", test, "\" | result:" ,ret)