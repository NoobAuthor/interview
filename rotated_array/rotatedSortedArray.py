# Problem: Rotated Sorted Array  (LeetCode 33)

# Given a rotated sorted array, find the index of a target element. If the target element is not found, return -1.

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if target >= nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            else:
                if target <= nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return - 1


# Test Cases
sol = Solution()
assert sol.search([4,5,6,7,0,1,2], 0) == 4
print('All test cases pass')
