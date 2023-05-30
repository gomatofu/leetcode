class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_price = prices[0]

        for p in prices:
            min_price = min(p,min_price)
            res = max(res,p - min_price)

        return res