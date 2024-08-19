from typing import *

# Problem: Minimum Coins
# Given a list of coin denominations and a target sum of money,
# find the minimum number of coins needed to make up the target sum.

class Solution:
    def minimumCoins(self, coins: List[int], target: int) -> int:
        dp = [float('inf')] * (target + 1) # Initialize dp array with infinity values 
        dp[0] = 0
        
        for i in range(1, target + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[target]

# Test Cases
sol = Solution()
assert sol.minimumCoins([1, 2, 5], 11) == 3
print('All test cases pass')