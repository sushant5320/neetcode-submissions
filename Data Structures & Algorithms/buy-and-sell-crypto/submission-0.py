class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # update sliding minimum (buy)
            if price < min_price:
                min_price = price
            
            # check profit if sold today
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit