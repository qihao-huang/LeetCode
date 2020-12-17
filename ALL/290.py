# https://leetcode-cn.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str_list = str.split(" ")
        pattern_dict = {}

        if len(str_list) != len(pattern):
            return False
        else:
            for i, j in zip(pattern, str_list):
                if i in pattern_dict.keys():
                    if pattern_dict[i] != j:
                        return False
                else:
                    if j in pattern_dict.values():
                        return False
                
                pattern_dict[i] = j

            return True