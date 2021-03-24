# https://leetcode-cn.com/problems/jump-game/


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        rightmost = 0

        for i in range(n):
            # 判断这个位置是可以被到达的
            if i <= rightmost:
                # 右侧最远处可到达的位置，需要被更新
                # 要么是原有的值，那么就是 i 位置 + nums[i]
                rightmost = max(rightmost, i+nums[i])

                # 如果超过了右边界，那么就是可以到达最远
                if rightmost > n - 1:
                    return True

        return False
        