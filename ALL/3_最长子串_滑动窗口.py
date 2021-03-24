# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)

        rk, ans = -1, 0

        for i in range(n):
            # 如果 while 循环被跳出，
            # 那么 check 左边界
            if i != 0:
                occ.remove(s[i-1])

            # 右指针不断移动，如果到了边界，或者下一个字母出现过
            # 那么就跳出 while 循环
            while rk + 1 < n and s[rk+1] not in occ:
                occ.add(s[rk+1])
                rk += 1
            
            ans = max(ans, rk-i+1)

        return ans