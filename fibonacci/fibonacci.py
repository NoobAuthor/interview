from typing import *

# Problem: Fibonacci

class Solution:
    def fibonacci(self, n: int) -> int:
        memo = {}

        for i in range(1, n+1):
            if i <= 2:
                result = 1
            else:
                result = memo[i] = memo[i - 1] + memo[i - 2]
            memo[i] = result 
        
        return memo[n]

    def recursive_fibonacci(self, n: int) -> int:
        memo = {}
        def helper(n):
            if n in memo:
                return memo[n]
            if n <= 2:
                return 1
            memo[n] = helper(n-1) + helper(n-2)
            return memo[n]
        return helper(n)


# Test Cases
sol = Solution()
assert sol.fibonacci(50) == 12586269025
print('All test cases pass')
assert sol.recursive_fibonacci(50) == 12586269025
print('All test cases pass')
