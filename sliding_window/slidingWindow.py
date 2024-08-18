from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left, right pointers
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1

        return max_profit

# Test the function
solution = Solution()
prices = [7, 1, 5, 3, 6, 4]
result = solution.maxProfit(prices)
print(result)  # Output should be 5

