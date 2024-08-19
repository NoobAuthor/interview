from typing import *

# Problem: Maximum Product Subarray
# Given an integer array nums, find the contiguous subarray within an array (containing at least one number)
# which has the largest product.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1
        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
                continue
            tmp = curMax
            curMax = max(n, n * curMax, n * curMin)
            curMin = min(n, n * tmp, n * curMin)
            res = max(res, curMax)
        return res
    
# Test Cases
sol = Solution()
assert sol.maxProduct([2,3,-2,4]) == 6
print('All test cases pass')

