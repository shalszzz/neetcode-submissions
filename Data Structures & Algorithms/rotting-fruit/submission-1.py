class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        x,y=len(grid),len(grid[0])
        time,fresh=0,0
        q=deque()

        for m in range(x):
            for n in range(y):
                if grid[m][n]==1:
                    fresh+=1
                elif grid[m][n]==2:
                    q.append([m,n])

        dirs=[[0,1],[0,-1],[1,0],[-1,0]]

        while q and fresh>0:

            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in dirs:
                    rows,cols= dr+r, dc+c
                    if (rows<0 or rows==x or cols<0 or cols==y or grid[rows][cols]!=1):
                        continue
                    grid[rows][cols]=2
                    q.append([rows,cols])
                    fresh-=1
            
            time+=1

        if fresh==0:
            return time 
        else:
            return -1



            
            
