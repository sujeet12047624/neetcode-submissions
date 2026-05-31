class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        maxprice=0
        n=len(prices)
        for i in range(1,n):
            if prices[i]>prices[l]:
                maxprice=max(maxprice,prices[i]-prices[l])
            else:
                l=i
        return maxprice

        