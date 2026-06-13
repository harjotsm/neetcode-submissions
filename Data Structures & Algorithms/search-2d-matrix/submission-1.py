class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l,r = 0, (ROWS * COLS) - 1

        while l <= r:
            mid = l + (r-l) // 2
            
            # 1D -> 2D
            row = mid // COLS
            col = mid % COLS
            mid_2d = matrix[row][col]

            if mid_2d == target:
                return True
            elif mid_2d < target:
                l = mid + 1
            else:
                r = mid-1
        return False