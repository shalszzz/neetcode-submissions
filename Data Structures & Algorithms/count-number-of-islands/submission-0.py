class Solution:
       
    def numIslands(self, grid: List[List[str]]) -> int:
        x=len(grid)
        y=len(grid[0])
        count=0

        def dfs(m,n):
            if m<0 or m>=x or n<0 or n>=y or grid[m][n]!="1":
                return
            grid[m][n]="0"
            dfs(m+1,n)
            dfs(m-1,n)
            dfs(m,n+1)
            dfs(m,n-1)


        for i in range (x):
            for j in range (y):
                if grid[i][j]=="1":
                    count+=1
                    dfs(i,j)    

        return count            
        

        
        