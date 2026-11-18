class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        buy = max(prices)
        maxProfit = 0

        for p in prices:
            if p < buy:
                buy = p
            profit = p - buy
            if profit > maxProfit:
                maxProfit = profit

        return(maxProfit)


prices = [10,8,7,5,2]

sol = Solution()
print(sol.maxProfit(prices))
