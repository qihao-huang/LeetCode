# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/

# greedy
# 贪心算法只能用于计算最大利润，计算的过程并不是实际的交易过程。
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1 <= prices.length <= 3 * 10 ^ 4
        # 0 <= prices[i] <= 10 ^ 4
        max_profit = 0
        for idx in range(1, len(prices)):
            max_profit += max(0, prices[idx]-prices[idx-1])

        return max_profit