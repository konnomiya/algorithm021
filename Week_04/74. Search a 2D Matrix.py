class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            pivot = matrix[mid // n][mid % n]
            if pivot == target:
                return True
            elif pivot > target:
                right = mid - 1
            elif pivot < target:
                left = mid + 1
        return False
