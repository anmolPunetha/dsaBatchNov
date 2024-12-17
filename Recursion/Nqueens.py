class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #0->empty, 1->placed queen
        grid  = [[0]*n for _ in range(n)]
        ans = []
        def isSafe(r,c):
            #col
            i,j=r,c
            while i>=0:
                if grid[i][j]==1:
                    return False
                i-=1
            
            #left diag->i,j=> i-1,j-1
            i,j=r,c
            while i>=0 and j>=0:
                if grid[i][j]==1:
                    return False
                i-=1
                j-=1

            #right diag->i,j=> i-1,j+1
            i,j=r,c
            while i>=0 and j<n:
                if grid[i][j]==1:
                    return False
                i-=1
                j+=1

            return True

        def helper(rowIdx):
            if rowIdx==n:
                #save
                l=[]
                for i in range(n):
                    s=""
                    for j in range(n):
                        if grid[i][j]==1:
                            s+='Q'
                        else:
                            s+='.'
                    l.append(s)
                ans.append(l)
                return
            
            for col in range(n):
                #rowIdx, col
                if isSafe(rowIdx,col):
                    grid[rowIdx][col]=1
                    helper(rowIdx+1)
                    grid[rowIdx][col]=0 #unplace

        helper(0)
        return ans
