class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr_lowest = prices[0]
        for i in prices:
            if i < curr_lowest: 
                curr_lowest = i
            else:
                profit = max(profit, i - curr_lowest)
        return profit

