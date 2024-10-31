class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        row=0
        col=n-1

        while col>=0 and row<m:
            val = matrix[row][col]
            if val==target:
                return True
            elif val>target:
                col-=1
            else:
                row+=1
        
        return False
