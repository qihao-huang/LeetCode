# https://leetcode-cn.com/problems/palindrome-permutation/

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # 初始化一个值为 0 的 dict/hashmap
        # 统计不同 key（字母）的出现频率
        # 回文字符串最多只能有一个 奇数次数 的 key
        freq_dict = defaultdict(int)
        for i in s:
            freq_dict[i] += 1

        odd_cnt = 0
        for key, value in freq_dict.items():
            if value % 2 == 1:
                odd_cnt += 1
                if odd_cnt > 1:
                    return False
        
        return True
