class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            m=len(matrix)
            n=len(matrix[0])
            left=0
            right=m*n-1
            while (left<=right):
                mid = left + (right - left) // 2
                row = mid // n
                col = mid % n
                mid_val = matrix[row][col]
                if mid_val<target:
                    left = mid + 1
                elif mid_val>target:
                    right=mid-1
                else:
                    return True
            return False