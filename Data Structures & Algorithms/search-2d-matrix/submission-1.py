class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        left_row, right_row = 0, rows - 1

        while left_row <= right_row:
            mid = (left_row + right_row)//2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                found_row = mid
                break
            elif matrix[mid][0] < target:
                left_row+=1
            else:
                right_row-=1
        
        found_row = mid
        left_col, right_col = 0, cols - 1

        while left_col <= right_col:
            mid = (left_col + right_col)//2

            if matrix[found_row][mid] == target:
                return True
            elif matrix[found_row][mid] < target:
                left_col+=1
            else:
                right_col-=1
        return False
        