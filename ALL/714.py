# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solution/


# 不能同时参与多笔交易
# 每天交易结束后只可能存在手里有一支股票或者没有股票的状态。

# （i 从 0 开始）
# dp[i][0] 表示第 i 天交易完后手里没有股票的最大利润
# dp[i][1] 表示第 i 天交易完后手里持有一支股票的最大利润
# 卖出时计算手续费

# 状态转移方程
# dp[0][0] = 0
# dp[0][1] = -prices[0]

#                            第 i 天买入卖出股票
# dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee) 

#                第 i 天买入股票
# dp[i][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0, -prices[0]]] + [[0, 0] for _ in range(n-1)]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee) 
            dp[i][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])

        return dp[n-1][0]