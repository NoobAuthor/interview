from typing import *

# Problem: Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.

class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSum = 0
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxSub = max(maxSub, currSum)
        
        return maxSub

# Test Cases
sol = Solution()
assert sol.maxSubarray([-2,1,-3,4,-1,2,1,-5,4]) == 6
