
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      profit = []
      for i in range(len(prices)):
        buy = prices[i]
        for j in range(i+1,len(prices)):
          sell = prices[j]
          if buy < sell:
            profit.append(sell-buy)
      if profit == []:
        return 0
      else:
        return max(profit)