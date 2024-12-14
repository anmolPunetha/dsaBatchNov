class Solution:
    # Function to find all possible paths
    def findPath(self, mat):
        all_paths = []
        n  = len(mat)
        
        dx = [-1, 0, 0, 1]
        dy = [0, 1, -1, 0]
        dir = ['U', 'R', 'L', 'D']
        def helper(i,j,path):
            #check if i am at a valid call
            if i<0 or j<0 or i==n or j==n or mat[i][j]!=1:
                return
            
            #i have reached the end
            if i==n-1 and j==n-1:
                #i have got a path and reached destination
                path_str = "".join(path)
                all_paths.append(path_str)
                return
            
            #calls
            mat[i][j] = 2 #visited/ part of the path
            
            #4 directions
            for k in range(3, -1, -1):
                ii = i+dx[k]
                jj = j+dy[k]
                path.append(dir[k])
                helper(ii,jj,path)
                path.pop()
            # #down-D
            # path.append('D')
            # helper(i+1,j,path)
            # path.pop()
            
            # #left-L
            # path.append('L')
            # helper(i,j-1,path)
            # path.pop()
            
            # #right - R
            # path.append('R')
            # helper(i,j+1,path)
            # path.pop()
            
            # #up->U
            # path.append('U')
            # helper(i-1,j,path)
            # path.pop()
            
            
            mat[i][j]=1 #make it unvisited
            
            
            
        helper(0,0,[])
        return all_paths
