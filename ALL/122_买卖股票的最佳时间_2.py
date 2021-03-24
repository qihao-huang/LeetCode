# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/

# greedy
# 贪心算法只能用于计算最大利润，计算的过程并不是实际的交易过程。
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1 <= prices.length <= 3 * 10 ^ 4
        # 0 <= prices[i] <= 10 ^ 4
        max_profit = 0
        # 贪心的角度考虑我们每次选择贡献大于 00 的区间即能使得答案最大化，因此最后答案为
        for idx in range(1, len(prices)):
            max_profit += max(0, prices[idx]-prices[idx-1])

        return max_profit

        # or
        # 动态规划的方法
        # 0 代表着不持有股票， 1 代表着持有股票
        # dp[i][0] = 第 i 天交易完后手头里没有股票的最大利润
        # dp[i][1] = 第 i 天交易完后手头里还有一支股票的最大利润
        # 第 i 天 dp[i][0] 可能由 dp[i-1][0] 造成，即第 i-1 天不购买股票
        # 或者第 i 天 卖出股票，那么
        # dp[i][0] = max{dp[i-1][0], dp[i-1][1]+prices[i]}

        # 同理
        # dp[i][1] = max{dp[i-1][1], dp[i-1][0]-prices[i]}
        
        # dp[0][0] = 0
        # dp[0][1] = -prices[0]

        # 最后 return dp[n-1][0]

        n = len(prices)

        dp_states = [ [0, 0] for i in range(n)]

        dp_states[0][0] = 0
        dp_states[0][1] = -prices[0]

        for i in range(1, n):
            dp_states[i][0] = max(dp_states[i-1][0], dp_states[i-1][1]+prices[i])
            dp_states[i][1] = max(dp_states[i-1][1], dp_states[i-1][0]-prices[i])


        return dp_states[n-1][0]