# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

# 遍历寻找最低价和相应的利润，返回最大值即可

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = int(1e9)
        max_profit = 0
        for day_price in prices:
            max_profit = max(day_price - min_price, max_profit)
            min_price = min(min_price, day_price)

        return max_profit
            