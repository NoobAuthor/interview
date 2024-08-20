from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i, n in enumerate(nums):
            value = target - n
            if value in res:
                return [res[value], i]
            res[n] = i
        
        return []


# Test the function
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(result)  # Output should be [0, 1]
