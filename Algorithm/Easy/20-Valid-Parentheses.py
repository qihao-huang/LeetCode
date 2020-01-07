# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Note that an empty string is also considered valid.

# Runtime: 24 ms, faster than 89.89% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.

class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True

        # ()
        # {}
        # []
        tmp_stack = []
        for item in s:
            if item in ("(", "[", "{"):
                tmp_stack.append(item)
            elif item == ")":
                if len(tmp_stack)>0 and tmp_stack[-1] == "(":
                    tmp_stack.pop()
                else:
                    return False
            elif item == "]":
                if len(tmp_stack)>0 and tmp_stack[-1] == "[":
                    tmp_stack.pop()
                else:
                    return False
            elif item == "}":
                if len(tmp_stack)>0 and tmp_stack[-1] == "{":
                    tmp_stack.pop()
                else:
                    return False
        
        return len(tmp_stack) == 0


# s = "{[]}" # true
s = "([)]" # false
# s = "(]" # false
# s = "()[]{}" # true
# s = "()" # true

ret = Solution().isValid(s)
out = (ret)
print(out)