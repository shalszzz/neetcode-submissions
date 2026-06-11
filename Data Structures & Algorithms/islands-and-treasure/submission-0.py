class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])

        def dfs(r, c, dist):
        
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == -1:
                return

            
            if grid[r][c] < dist:
                return

            grid[r][c] = dist

            dfs(r + 1, c, dist + 1)
            dfs(r - 1, c, dist + 1)
            dfs(r, c + 1, dist + 1)
            dfs(r, c - 1, dist + 1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    dfs(r, c, 0)