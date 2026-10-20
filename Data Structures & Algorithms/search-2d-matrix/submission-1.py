class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Brute force O(N^2)
        # for row in matrix:
        #     for i in range(len(row)):
        #         if row[i] == target:
        #             return True
        
        # return False

        # ******************************
        # Binary Search:
        if not matrix or not matrix[0]:
            return False
            
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        
        while top <= bottom:
            middleRow = (top + bottom) // 2
            if matrix[middleRow][0] <= target <= matrix[middleRow][-1]:
                rowToCheck = middleRow
                break
            elif matrix[middleRow][0] > target:
                bottom = middleRow - 1
            else:
                top = middleRow + 1
        else:
            return False
            
        left, right = 0, cols - 1
        
        while left <= right:
            middleCol = (left + right) // 2
            if matrix[rowToCheck][middleCol] == target:
                return True
            elif matrix[rowToCheck][middleCol] < target:
                left = middleCol + 1
            else:
                right = middleCol - 1
                
        return False
