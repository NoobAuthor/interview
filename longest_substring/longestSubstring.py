from typing import *

# Longest Substring Without Repeating Characters

class Solution:
    def longestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 0
        res = 0
        seen = set()
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                res = max(res, r - l + 1) # Update the result if the current substring is longer than the previous one
                r += 1
            else:
                seen.remove(s[l])   # Remove the leftmost character from the set if it is already in the set
                l += 1
        return res

# Test the function
solution = Solution()
s = "abcabcbb"
result = solution.longestSubstring(s)
print(result)  # Output should be 3
