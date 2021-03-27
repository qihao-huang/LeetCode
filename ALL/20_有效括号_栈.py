# https://leetcode-cn.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        
        valid_bracket = {
            ")": "(", 
            "}": "{", 
            "]": "[",
        }

        stack = []

        for item in s:
            if item in valid_bracket:
                if not stack or stack[-1] != valid_bracket[item]:
                # 如果 stack 已经为空，那么当前的括号无法被匹配到
                # 或者如果前一个元素和当前的括号不匹配
                    return False
                stack.pop()
            else:
                stack.append(item)

        # 如果 stack 为空，说明括号都已经被匹配到
        return not stack

        

