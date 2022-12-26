from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if len(prices)<=1: return 0
        # if len(prices)==2: return prices[-1]-prices[0] if prices[-1]>prices[0] else 0

        # start=0
        # while start<len(prices)-1 and prices[start]>=prices[start+1]: start+=1

        # if start == len(prices)-1: return 0
        # prices= prices[start:]

        # M= max(prices)
        # m= min(prices[:prices.index(M)]) if prices[:prices.index(M)] else float("inf")
        # result= 0 if m>M else M-m

        # return max(result, Solution().maxProfit(prices[prices.index(M)+1:]))
        
        buy= float("inf")
        profit= 0
        for price in prices:
            if price<buy: buy= price
            elif price-buy>profit: profit= price - buy
        
        return profit