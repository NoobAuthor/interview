from typing import *

# Given an integer array nums, return an array answer such that answer[i],
# is equal to the product of all the elements of nums except nums[i].

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        left_product = 1
        for i in range(len(nums)):
            res[i] = left_product
            left_product *= nums[i]
        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]
        return res

# Test the function
solution = Solution()
nums = [1, 2, 3, 4]
result = solution.productExceptSelf(nums)
print(result)  # Output should be [24, 12, 8, 6]
