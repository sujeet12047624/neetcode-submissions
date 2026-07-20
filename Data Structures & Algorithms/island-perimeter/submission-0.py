class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        m=len(grid)
        n=len(grid[0])
        st=set()
        ans=0
        def dfs(r,c):

            if r<0 or r>=m or c<0 or c>=n or  grid[r][c]==0:
                return 1
            if (r,c) in st :
                return 0
            st.add((r,c))
            p=dfs(r,c+1)+dfs(r,c-1)+dfs(r+1,c)+dfs(r-1,c)
            return p
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                   return dfs(i,j)
        return 0
            
            
            
        