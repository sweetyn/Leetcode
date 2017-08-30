"""121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0."""

class Solution(object):
    def maxProfit(self, prices):

        tempMax = 0
        i = 1
        for x in prices:
            for j in range(len(prices)-i):
                if x < prices[i+j]:
                    if tempMax < prices[i+j] - x:
                        tempMax = prices[i+j] - x
            i += 1

        return tempMax

prices = [7, 1, 5, 3, 6, 4]
test1 = Solution()

print(test1.maxProfit(prices))
#completed in 20mins
