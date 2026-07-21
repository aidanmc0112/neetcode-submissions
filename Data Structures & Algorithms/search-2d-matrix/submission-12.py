class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        
        cols = len(matrix[0])-1
        while left <= right and cols >= 0:
            if target > matrix[left][cols]:
                left+=1
            elif target == matrix[left][cols]:
                return True
            else:
                cols-=1
        return False
