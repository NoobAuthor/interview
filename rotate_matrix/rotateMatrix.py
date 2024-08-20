from typing import *

# Rotate Matrix 90 degrees clockwise

class Solution:
    def rotateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for row in matrix:  # Reverse each row of the matrix to get the 90 degrees clockwise rotated matrix
            row.reverse() # Reverse the row in place using the reverse() method 
        
        return matrix


# Test the function
solution = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = solution.rotateMatrix(matrix)
print(result)  # Output should be [[7, 4, 1], [8, 5, 2], [9, 6, 3]]