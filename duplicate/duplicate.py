from typing import *

# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

# Test the function
solution = Solution()
nums = [1, 2, 3, 1]
result = solution.containsDuplicate(nums)
print(result)  # Output should be True
