from typing import *

# Reverse string

class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        return s
        


# Test the function
solution = Solution()
s = ["h", "e", "l", "l", "o"]
result = solution.reverseString(s)
print(result)  # Output should be ["o", "l", "l", "e", "h"]