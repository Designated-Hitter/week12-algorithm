class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_price = prices[0]
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                result = max(result, price - min_price)
        return result