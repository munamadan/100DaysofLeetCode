#brute force method (while it's correct, it exceeds runtime because it has O(n^2) runtime)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        diff = 0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                j=i+1
                while j<len(prices):
                    diff = max(prices[j]-prices[i], diff)
                    j+=1
        return diff
    
#optimized solution
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minPrice = prices[0]
        res=0
        for i in range(len(prices)):
            res=max(res, prices[i]-minPrice)
            minPrice=min(minPrice, prices[i])
        return res
    
#neetcode two pointer method
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l,r = 0,1
        maxProfit=0
        while r<len(prices):
            if prices[r]<prices[l]:
                l=r
            else:
                maxProfit=max(maxProfit, prices[r]-prices[l])
            r+=1
        return maxProfit